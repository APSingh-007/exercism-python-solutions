from itertools import permutations as perms


def solve(puzzle: str) -> dict[str:int]:
    left, right = puzzle.split(" == ")
    words: list[str] = []
    result = right[::-1]
    letters = set(result)

    for word in left.split(" + "):
        word = word.strip()[::-1]
        words.append(word)
        letters |= set(word)

    height = len(words)
    width = len(result)
    total_letters = len(letters)

    if total_letters > 10:
        raise ValueError("More than 10 letter found. Can't have more values than 0-9.")

    def check_permutation(letter_map: dict[str:int]) -> bool:
        sum_string = ""
        previous_carry = 0

        for i in range(width):
            vertical_sum = 0
            for h in range(height):
                word = words[h]

                if len(word) > width:
                    return False

                if len(word) <= i:
                    continue
                else:
                    vertical_sum += letter_map[word[i]]

            vertical_sum += previous_carry
            previous_carry = vertical_sum // 10
            vertical_sum %= 10
            sum_string += str(vertical_sum)

            if vertical_sum != letter_map[result[i]]:
                return False

        return True

    first_letters = [word[-1] for word in words] + [result[-1]]

    def first_letter_is_0(letter_map: dict[str:int]):
        for fl in first_letters:
            if letter_map[fl] == 0:
                return True

    first_letters = [word[-1] for word in words] + [result[-1]]
    for digits in perms(range(10), r=len(letters)):
        letter_map = dict(zip(letters, digits))
        if first_letter_is_0(letter_map):
            continue

        if check_permutation(letter_map):
            return {key: letter_map[key] for key in sorted(letter_map.keys())}


puzzle = "HE + SEES + THE == LIGHT"
print(solve(puzzle))
