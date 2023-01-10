from datetime import date


def get_date_string() -> str:
    """This function creates a date:
    Arguments:
        [None]
    Returns:
        [str] -- Возвращает текущую дату в формате Год-Месяц-День"""
    return date.today().strftime("%Y-%m-%d")


print(get_date_string())
