ERRORS = {
    "l<10": "must not be fewer than 10 digits",
    "l>11": "must not be greater than 11 digits",
    "cn1": "11 digits must start with 1",
    "exch": "exchange code cannot start with",
    "area": "area code cannot start with",
    "punc": "punctuations not permitted",
    "lttr": "letters not permitted",
}


class PhoneNumber:
    def __init__(self, number: str):
        self.number, self.area_code, self.exchange_code = self.get_num(number)

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.number[-4:]}"

    def get_num(self, number: str) -> tuple[str]:
        num = ""
        length = 0
        for d in number:
            if d.isdigit():
                num += d
                length += 1
                continue
            if d.isalpha():
                raise ValueError(ERRORS["lttr"])
            if d not in ".+() -":
                raise ValueError(ERRORS["punc"])

        country_code = num[0] if length == 11 else None

        if length < 10:
            raise ValueError(ERRORS["l<10"])
        if length > 11:
            raise ValueError(ERRORS["l>11"])

        num = num[-10:]
        area = num[0:3]
        exchange = num[3:6]

        if length == 11 and country_code != "1":
            raise ValueError(ERRORS["cn1"])
        if area[0] in "01":
            raise ValueError(f'{ERRORS["area"]} {("zero", "one")[int(area[0])]}')
        if exchange[0] in "01":
            raise ValueError(f'{ERRORS["exch"]} {("zero", "one")[int(exchange[0])]}')

        return (num, area, exchange)
