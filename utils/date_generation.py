from datetime import date


def get_date_string() -> str:
    """_summary_
        This function creates a date

    Parameters
    ----------
    [None]

    Returns
    -------
    _type_ [str]
        Returns the current date in Year-Month-Day format
    """
    return date.today().strftime("%Y-%m-%d")
