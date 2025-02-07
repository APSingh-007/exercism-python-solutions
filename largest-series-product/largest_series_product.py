import math


def largest_product(input_series: str, span: int) -> int:
    input_len = len(input_series)

    if span > input_len:
        raise ValueError("span must be smaller than string length")
    if span <= 0:
        raise ValueError("span must not be negative")
    if not input_series.isdigit():
        raise ValueError("digits input must only contain digits")

    products: list[int] = []
    for index in range(input_len - span + 1):
        series: list[int] = [int(num) for num in input_series[index : index + span]]
        products.append(math.prod(series))

    return max(products)
