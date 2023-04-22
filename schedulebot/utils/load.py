import pandas as pd


def weekdays():
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    df = pd.DataFrame(weekdays)
    return (df)


def get_time_intervals():
    time_intervals = ['8:00 - 9:30',
                      '9:50 - 11:20',
                      '11:40-13:10',
                      '13:40-15:10',
                      '15:30-17:00',
                      '17:20-18:50']
    df = pd.DataFrame(time_intervals)
    return (df)
