from src.pre_built.brazilian_jobs import read_brazilian_file
from tests.mocks.english_jobs import mock_english


def test_brazilian_jobs():
    result = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    print(mock_english)
    assert result == mock_english
