# def decode(string: str) -> str:
#     if not string:
#         return ""
#     decompressed = ""
#     count = ""
#     for char in string:
#         if char.isdigit():
#             count += char
#         else:
#             decompressed += char * int(count or 1)
#             count = ""
#     return decompressed


# def encode(string: str) -> str:
#     if not string:
#         return ""
#     compressed = ""
#     count = 1
#     prev_char = string[0]

#     for char in string[1:]:
#         if char == prev_char:
#             count += 1
#         else:
#             compressed += str(count) + prev_char if count > 1 else prev_char
#             count = 1
#             prev_char = char

#     compressed += str(count) + prev_char if count > 1 else prev_char
#     return compressed

import re
from itertools import groupby


def encode(s):
    compressed = ""
    for char, group in groupby(s):
        gr = "".join(i for i in group)
        print(char, gr)
        count = len(list(group))
        compressed += str(count) + char if count > 1 else char
    return compressed


def decode(s):
    decompressed = ""
    for count, char in re.findall(r"(\d+)?(.)", s):
        decompressed += char * int(count or 1)
    return decompressed


# Test the functions
input_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
compressed_string = encode(input_string)
print("Compressed:", compressed_string)  # Output: "12WB12W3B24WB"
decompressed_string = decode(compressed_string)
print(
    "Decompressed:", decompressed_string
)  # Output: "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
