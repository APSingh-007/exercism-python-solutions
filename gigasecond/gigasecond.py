import datetime


def add(moment):
    td = datetime.timedelta(seconds=1_000_000_000)
    return moment + td
