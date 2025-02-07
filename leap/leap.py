def leap_year(year: int) -> bool:
    return not (year % 4 if year % 100 else year % 400)
