from src.pre_built.sorting import sort_by
import pytest

jobs_mock = [
    {
        "job_title": "Emergency Veterinarian - NYC",
        "min_salary": "94715",
        "max_salary": "103279",
        "date_posted": "2020-05-05",
    },
    {
        "job_title": "Diesel Mechanic",
        "min_salary": "46298",
        "max_salary": "55893",
        "date_posted": "2020-05-01",
    },
    {
        "job_title": "OT/ICS Systems Engineer",
        "min_salary": "122296",
        "max_salary": "148734",
        "date_posted": "2020-04-28",
    },
    {
        "job_title": "Emergency Veterinary Technician",
        "min_salary": "38471",
        "max_salary": "43006",
        "date_posted": "2020-05-08",
    },
    {
        "job_title": "undefined",
        "min_salary": "",
        "max_salary": "",
        "date_posted": "",
    },
]

jobs_sort_date = [
    {
        "job_title": "Emergency Veterinary Technician",
        "min_salary": "38471",
        "max_salary": "43006",
        "date_posted": "2020-05-08",
    },
    {
        "job_title": "Emergency Veterinarian - NYC",
        "min_salary": "94715",
        "max_salary": "103279",
        "date_posted": "2020-05-05",
    },
    {
        "job_title": "Diesel Mechanic",
        "min_salary": "46298",
        "max_salary": "55893",
        "date_posted": "2020-05-01",
    },
    {
        "job_title": "OT/ICS Systems Engineer",
        "min_salary": "122296",
        "max_salary": "148734",
        "date_posted": "2020-04-28",
    },
    {
        "job_title": "undefined",
        "min_salary": "",
        "max_salary": "",
        "date_posted": "",
    },
]

jobs_sort_max = [
    {
        "job_title": "OT/ICS Systems Engineer",
        "min_salary": "122296",
        "max_salary": "148734",
        "date_posted": "2020-04-28",
    },
    {
        "job_title": "Emergency Veterinarian - NYC",
        "min_salary": "94715",
        "max_salary": "103279",
        "date_posted": "2020-05-05",
    },
    {
        "job_title": "Diesel Mechanic",
        "min_salary": "46298",
        "max_salary": "55893",
        "date_posted": "2020-05-01",
    },
    {
        "job_title": "Emergency Veterinary Technician",
        "min_salary": "38471",
        "max_salary": "43006",
        "date_posted": "2020-05-08",
    },
    {
        "job_title": "undefined",
        "min_salary": "",
        "max_salary": "",
        "date_posted": "",
    },
]

jobs_sort_min = [
    {
        "job_title": "Emergency Veterinary Technician",
        "min_salary": "38471",
        "max_salary": "43006",
        "date_posted": "2020-05-08",
    },
    {
        "job_title": "Diesel Mechanic",
        "min_salary": "46298",
        "max_salary": "55893",
        "date_posted": "2020-05-01",
    },
    {
        "job_title": "Emergency Veterinarian - NYC",
        "min_salary": "94715",
        "max_salary": "103279",
        "date_posted": "2020-05-05",
    },
    {
        "job_title": "OT/ICS Systems Engineer",
        "min_salary": "122296",
        "max_salary": "148734",
        "date_posted": "2020-04-28",
    },
    {
        "job_title": "undefined",
        "min_salary": "",
        "max_salary": "",
        "date_posted": "",
    },
]


print(jobs_mock)


def test_sort_by_criteria():
    sort_by(jobs_mock, "min_salary")
    assert jobs_mock == jobs_sort_min

    sort_by(jobs_mock, "max_salary")
    assert jobs_mock == jobs_sort_max

    sort_by(jobs_mock, "date_posted")
    assert jobs_mock == jobs_sort_date

    with pytest.raises(ValueError):
        sort_by(jobs_mock, "undefined")

    with pytest.raises(ValueError):
        sort_by(jobs_mock, "date_post")
