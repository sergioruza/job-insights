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
    jobs_by_type = []

    for job in jobs:
        if job["job_type"] == job_type:
            jobs_by_type.append(job)
    return jobs_by_type
