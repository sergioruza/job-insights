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
            raise ValueError("verifica se existe")

        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary_num = int(salary)

        verify_num = min_salary > max_salary

        if verify_num:
            raise ValueError("numero min nao")

        return min_salary <= salary_num <= max_salary

    except (ValueError, KeyError, TypeError) as e:
        raise ValueError(f"{e.args[0]}")


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    list_jobs = []

    for job in jobs:
        try:
            job_c = {
                "max_salary": int(job["max_salary"]),
                "min_salary": int(job["min_salary"]),
            }

            if matches_salary_range(job_c, salary):
                list_jobs.append(job)
        except (ValueError, KeyError, TypeError):
            pass

    return list_jobs


#  Referencia de ajuda Arthur Debiasi
