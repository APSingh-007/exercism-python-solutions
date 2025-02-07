# Iteration with backtracking, still slower than bethanyG and uses more memory
from itertools import permutations as perm


class valid_perm:
    def __init__(self, col_no: int, hash_map: dict[str:int], carry: int) -> None:
        self.col_no = col_no
        self.hash_map = hash_map
        self.carry = carry


def solve(puzzle: str) -> dict[str:int]:
    # left part contains equation (W + W + W), right part (last word) contains result
    left, right = (string.strip() for string in puzzle.split("=="))
    result = list(right[::-1])  # last word is the result of alphabetic equation
    # width must le len(result) or some word's first letter must be 0, which is not possible
    width = len(result)
    words = []  # shall contain the words that would be added

    # initialise all_letters with letters from result and later ass the letters from word
    all_letters = set(result)
    first_letters = {result[-1]}  # similar as first_letters
    stack: list[valid_perm] = []

    # populate words, all_letters, first_letters
    for word in left.split("+"):
        word = list(reversed(word.strip()))
        words.append(word)
        all_letters.update(word)
        first_letters.add(word[-1])

    def get_validity_and_carry(
        hash_map: dict[str:int], vertical_ltrs: list[str], carry: int, res_ltr: str
    ) -> tuple[bool, int]:
        vertical_sum = carry

        for ltr in vertical_ltrs:
            vertical_sum += hash_map[ltr]

        carry = vertical_sum // 10
        return (hash_map[res_ltr] == vertical_sum % 10, carry)

    def get_perms(
        hash_map: dict[str:int],
        col_no: int,
        carry: int,  # carry from previous column (is 0 for column = 0)
    ) -> list[valid_perm]:
        """
        Returns valid permutations of hashmaps, and their respective carry for the current coloumn (col_no)

        vertical_ltrs  : contains the letters in current column of all words( except from result)
        allowed_digits : contains digits (in range(10)) that are not present in hashmap values
        ltrs_to_perm   : contains letters in current column of all words (including result) which are not mapped to a value in hash_map
        """
        vertical_ltrs = [word[col_no] for word in words if col_no < len(word)]
        res_ltr = result[col_no]
        allowed_digits = [d for d in range(10) if d not in hash_map.values()]
        ltrs_to_perm = [
            ltr for ltr in set(vertical_ltrs + [res_ltr]) if ltr not in hash_map.keys()
        ]
        non_zero_ltrs = []
        other_ltrs = []
        valid_perms: list[valid_perm] = []

        for ltr in ltrs_to_perm:
            if ltr in first_letters:
                non_zero_ltrs.append(ltr)
            else:
                other_ltrs.append(ltr)

        digits = allowed_digits.copy()
        if 0 in digits:
            digits.remove(0)

        for nums_non_zero in perm(digits, r=len(non_zero_ltrs)):
            digits = [d for d in allowed_digits if d not in nums_non_zero]
            temp_hash_map = dict(zip(non_zero_ltrs, nums_non_zero))

            # def check_perms ()
            for other_nums in perm(digits, r=len(other_ltrs)):
                hash_map = hash_map | temp_hash_map | dict(zip(other_ltrs, other_nums))

                valid, local_carry = get_validity_and_carry(
                    hash_map, vertical_ltrs, carry, res_ltr
                )
                if valid:
                    valid_perms.append(valid_perm(col_no, hash_map, local_carry))

        return valid_perms

    stack.extend(
        get_perms(
            hash_map={},
            col_no=0,
            carry=0,
        )
    )
    while stack:
        current_perm = stack.pop()

        if current_perm.col_no == width - 1 and current_perm.carry == 0:
            return current_perm.hash_map

        next_perms = get_perms(
            hash_map=current_perm.hash_map,
            col_no=current_perm.col_no + 1,
            carry=current_perm.carry,
        )

        if not next_perms:
            continue
        stack.extend(next_perms)
    else:
        return None
