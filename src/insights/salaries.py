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
    verify_exists = "min_salary" not in job and "max_salary" not in job
    verify_num = job["min_salary"] < job["max_salary"]
    verify_type_num = isinstance(job["min_salary"], int)
    if verify_exists and verify_num and verify_type_num:
        raise ValueError("seila")

    if salary < job["max_salary"] and salary > job["min_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
