from datetime import datetime, date

WEEKS: dict = {"first": 0, "second": 1, "third": 2, "fourth": 3, "fifth": 4, "last": -1}
DAYS: tuple = (
    "",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)


# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(Exception):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """

    def __init__(self, err, message="That day does not exist."):
        self.err = err
        self.message = message
        return super().__init__(self.message)


def days_in_month(year: int, month: int) -> int:
    current_month_day1 = datetime(year, month, 1)

    year, month = (year + 1, 1) if month == 12 else (year, month + 1)
    next_month_day1 = datetime(year, month, 1)

    return (next_month_day1 - current_month_day1).days


def meetup(year: int, month: int, week: str, day_of_week: str) -> datetime.date:
    day: int = DAYS.index(day_of_week)

    first_day: int = (
        date(year, month, 1).isoweekday()
        if week != "teenth"
        else date(year, month, 13).isoweekday()
    )

    how_far = day - first_day if day >= first_day else (7 - first_day) + day
    total_days = days_in_month(year, month)

    days_matching: list[int] = (
        [13 + how_far]
        if week == "teenth"
        else [x for x in range(1 + how_far, total_days + 1, 7)]
    )

    try:
        required_day = (
            days_matching[0] if week == "teenth" else days_matching[WEEKS[week]]
        )
    except IndexError as err:
        raise MeetupDayException(err)

    return date(year, month, required_day)
