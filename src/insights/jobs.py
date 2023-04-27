from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        data = csv.DictReader(file)
        return [row for row in data]


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    filter_jobs = set()
    for job in data:
        filter_jobs.add(job["job_type"])
    return filter_jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError


read("data/jobs.csv")
