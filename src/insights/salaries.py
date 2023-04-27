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
        verify_exists = "min_salary" not in job or "max_salary" not in job
        if verify_exists:
            raise ValueError("seila vo dormi")

        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary_num = int(salary)

        verify_num = min_salary > max_salary

        if verify_num:
            raise ValueError("seila")

        return min_salary <= salary_num <= max_salary

    except (ValueError, KeyError, TypeError):
        raise ValueError("seila")


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
