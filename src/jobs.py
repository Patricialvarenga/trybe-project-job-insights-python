import csv
from functools import lru_cache


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
      List of rows as dicts
    """
    with open(path, "r") as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        job_list = list(jobs_reader)
        return job_list
