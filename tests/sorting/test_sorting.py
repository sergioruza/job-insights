from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    result = sort_by("data/jobs.csv", "min_salary")
    print("aquiii", result)
