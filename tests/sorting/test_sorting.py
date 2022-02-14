from src.sorting import sort_by

mock_jobs = [
    {"max_salary": 10, "min_salary": 100, "date_posted": "2022-02-14"},
    {"max_salary": 100, "min_salary": 1000, "date_posted": "2022-02-15"},
    {"max_salary": 10000, "min_salary": 500, "date_posted": "2022-02-16"},
    {"max_salary": 20000, "min_salary": 200, "date_posted": "2022-02-17"},
]

mock_jobs_by_min_salary = [
    {"max_salary": 10, "min_salary": 100, "date_posted": "2022-02-14"},
    {"max_salary": 20000, "min_salary": 200, "date_posted": "2022-02-17"},
    {"max_salary": 10000, "min_salary": 500, "date_posted": "2022-02-16"},
    {"max_salary": 100, "min_salary": 1000, "date_posted": "2022-02-15"},
]

mock_jobs_by_max_salary = [
    {"max_salary": 20000, "min_salary": 200, "date_posted": "2022-02-17"},
    {"max_salary": 10000, "min_salary": 500, "date_posted": "2022-02-16"},
    {"max_salary": 100, "min_salary": 1000, "date_posted": "2022-02-15"},
    {"max_salary": 10, "min_salary": 100, "date_posted": "2022-02-14"},
]

mock_jobs_by_date_posted = [
    {"max_salary": 20000, "min_salary": 200, "date_posted": "2022-02-17"},
    {"max_salary": 10000, "min_salary": 500, "date_posted": "2022-02-16"},
    {"max_salary": 100, "min_salary": 1000, "date_posted": "2022-02-15"},
    {"max_salary": 10, "min_salary": 100, "date_posted": "2022-02-14"},
]

criterias = ("min_salary", "max_salary", "date_posted")


def test_sort_by_criteria():
    sort_by(mock_jobs, criterias[0])
    assert mock_jobs == mock_jobs_by_min_salary

    sort_by(mock_jobs, criterias[1])
    assert mock_jobs == mock_jobs_by_max_salary

    sort_by(mock_jobs, criterias[2])
    assert mock_jobs == mock_jobs_by_date_posted
