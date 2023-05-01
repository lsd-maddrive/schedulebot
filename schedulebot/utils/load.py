from typing import List


def weekdays() -> List[str]:
    """The function should return a list of lines with weekdays"""

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return (weekdays)


def get_time_intervals() -> List[str]:
    """The function should return a list of lines with learning intervals"""

    time_intervals = ['8:00 - 9:30',
                      '9:50 - 11:20',
                      '11:40 - 13:10',
                      '13:40 - 15:10',
                      '15:30 - 17:00',
                      '17:20 - 18:50']
    return (time_intervals)


def split_name(list):
    i = 0
    cash = ''
    middle_name = []
    first_name = []
    last_name = []
    while i < len(list):
        j = 0
        while list[i][j] != ' ':
            cash += list[i][j]
            j += 1
        middle_name.append(cash)
        cash = ''
        j += 1
        while list[i][j] != ' ':
            cash += list[i][j]
            j += 1
        first_name.append(cash)
        cash = ''
        j += 1
        while j < len(list[i]):
            cash += list[i][j]
            j += 1
        last_name.append(cash)
        cash = ''
        i += 1
    return(middle_name, first_name, last_name)
