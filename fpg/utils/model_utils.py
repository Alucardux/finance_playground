"""
Utils will contain the shared functions across tasks
"""


def compute_year_month(year, month):
    """
    Compute year-month

    Args:
        year: year as yyyy
        month: month as mm

    Returns: yyyy * 100 + mm

    """

    return year * 100 + month