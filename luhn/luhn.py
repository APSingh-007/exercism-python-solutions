class Luhn:
    def __init__(self, card_num: str):
        self.card_num = card_num

    def valid(self) -> bool:
        total = 0

        numbers = [*(self.card_num.replace(" ", ""))]

        for i, num in enumerate(reversed(numbers)):
            try:
                if i % 2 != 0:
                    n = int(num) * 2
                    total += n if n < 9 else n - 9
                else:
                    total += int(num)
            except ValueError:
                return False

        return total % 10 == 0 and (total != 0 or len(numbers) > 1)
