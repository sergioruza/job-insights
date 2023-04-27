from src.pre_built.counter import count_ocurrences


def test_counter():
    result = count_ocurrences("data/jobs.csv", "python")
    assert result == 1639


# js - 122
# python 1639
