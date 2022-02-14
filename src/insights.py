from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    job_list = read(path)
    job_unique_type_list = []
    for job in job_list:
        job_unique_type_list.append(job["job_type"])
    return set(job_unique_type_list)


def filter_by_job_type(jobs, job_type):
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
    job_list_with_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_list_with_job_type.append(job)
    return job_list_with_job_type


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    industry_list = read(path)
    industry_unique_list = []
    for industry in industry_list:
        if industry["industry"]:
            industry_unique_list.append(industry["industry"])
    return set(industry_unique_list)


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    job_list_by_industry = []
    for job in jobs:
        if job["industry"] == industry:
            job_list_by_industry.append(job)
    return job_list_by_industry


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    # O método isdigit , embutido no tipo str , pode ser utilizado para
    #  verificar se a string corresponde a um número natural.
    # Uso do max: https://www.w3schools.com/python/ref_func_max.asp
    job_list = read(path)
    salary_list = []
    for salary in job_list:
        if salary["max_salary"].isdigit():
            salary_list.append(int(salary["max_salary"]))
    max_salary = max(salary_list)
    return max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    # O método isdigit , embutido no tipo str , pode ser utilizado para
    #  verificar se a string corresponde a um número natural.
    # Uso do min: https://www.w3schools.com/python/ref_func_min.asp
    job_list = read(path)
    salary_list = []
    for salary in job_list:
        if salary["min_salary"].isdigit():
            salary_list.append(int(salary["min_salary"]))
    min_salary = min(salary_list)
    return min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    # Uso do raise: https://docs.python.org/3/library/exceptions.html
    if ("min_salary" not in job or "max_salary" not in job):
        raise ValueError('Min_salary or max_salary does not exists')
    elif (type(job["max_salary"]) != int or type(job["min_salary"]) != int):
        raise ValueError('Max_salary or min_salary are not valid integers')
    elif(type(salary) != int):
        raise ValueError('Salary is not a valid integer')
    elif (job["min_salary"] > job["max_salary"]):
        raise ValueError('Min_salary salary is greater than max_salary!')
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
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
    # Uso do pass: https://www.w3schools.com/python/ref_keyword_pass.asp
    job_list_by_salary_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                job_list_by_salary_range.append(job)
        except ValueError:
            pass
    return job_list_by_salary_range
