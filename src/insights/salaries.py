from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)

    salary = set()
    for job in data:
        if job["max_salary"].isdigit():
            salary.add(int(job["max_salary"]))
    return max(salary)


def get_min_salary(path: str) -> int:
    data = read(path)

    salary = set()
    for job in data:
        if job["min_salary"].isdigit():
            salary.add(int(job["min_salary"]))
    return min(salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        verify_exists = "min_salary" not in job and "max_salary" not in job
        verify_num = job["min_salary"] < job["max_salary"]
        verify_type_num = isinstance(job["min_salary"], int)
        if verify_exists and verify_num and verify_type_num:
            raise ValueError

        if salary < job["max_salary"] and salary > job["min_salary"]:
            return True
        else:
            return False
    except ValueError:
        print("erro aqui hein")
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    list_jobs = []

    for job in jobs:
        if isinstance(job["min_salary"], int) and isinstance(
            job["max_salary"], int
        ):
            job = {
                "max_salary": int(job["max_salary"]),
                "min_salary": int(job["min_salary"]),
            }

            if matches_salary_range(job, salary):
                list_jobs.append(job)

    return list_jobs
