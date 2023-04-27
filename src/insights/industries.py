from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)

    filter_industries = set()
    for job in data:
        if job["industry"] != "":
            filter_industries.add(job["industry"])
    return filter_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    jobs_by_type = []

    for job in jobs:
        if job["industry"] == industry:
            jobs_by_type.append(job)
    return jobs_by_type
