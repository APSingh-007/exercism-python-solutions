from datetime import datetime


class LedgerEntry:
    def __init__(self, date: str, description: str, change: str) -> None:
        self.date: datetime = datetime.strptime(date, "%Y-%m-%d")
        self.description = description
        self.change = change


create_entry = LedgerEntry


def format_entries(currency: str, locale: str, entries: list[LedgerEntry]) -> str:
    # Generate Header Row
    if locale == "en_US":
        table = f"{'Date':<11}| {'Description':<26}| {'Change':<13}"
        seperator, decimal_symbol = (",", ".")
    elif locale == "nl_NL":
        table = f"{'Datum':<11}| {'Omschrijving':<26}| {'Verandering':<13}"
        seperator, decimal_symbol = (".", ",")
    else:
        raise ValueError("Unknown Locale")

    # Sort entries by date and change amount in ascending order
    entries.sort(key=lambda entry: (entry.date, entry.change))

    # Format Change in accordance with the region and currency
    def format_change(change: int) -> str:
        negative = change < 0
        change = abs(change)
        number_part = ""
        decimal_part = str(change % 100).rjust(2, "0")
        change = str(change // 100)

        current_part = ""
        for n in reversed(change):
            current_part += n
            if len(current_part) == 3:
                number_part = seperator + current_part[::-1] + number_part
                current_part = ""
        else:
            if current_part:
                number_part = current_part[::-1] + number_part

        symbol = "$" if currency == "USD" else "€"
        number = f"{number_part.strip(seperator)}{decimal_symbol}{decimal_part}"

        if negative:
            return (
                f"({symbol}{number})" if locale == "en_US" else f"{symbol} -{number} "
            )
        else:
            return f"{symbol}{number} " if locale == "en_US" else f"{symbol} {number} "

    # Truncate description if necessary
    def format_description(description: str) -> str:
        return description[:22] + "..." if len(description) > 25 else description

    # Format date as per the Locale
    def format_date(date: datetime) -> str:
        formats: dict = {
            "en_US": "%m/%d/%Y",
            "nl_NL": "%d-%m-%Y",
        }
        return date.strftime(formats[locale])

    # Read sorted entries and format the table
    for entry in entries:
        date = format_date(entry.date)
        desc = format_description(entry.description)
        change = format_change(entry.change)
        table += f"\n{date:<11}| {desc:<26}| {change:>13}"

    return table
