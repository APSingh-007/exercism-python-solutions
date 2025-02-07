from itertools import permutations, chain, product
from time import sleep


def dig_perms(digit_set, non_zero_chars, ok_zero_chars):
    non_zeros = len(non_zero_chars)
    zeros_ok = len(ok_zero_chars)
    total_count = non_zeros + zeros_ok

    non_zero_digits = digit_set - set((0,))
    available_zero_digits = len(non_zero_digits)
    ok_zero_digits = len(digit_set)

    if total_count < 1:
        return [()]

    elif (ok_zero_digits < total_count) or (available_zero_digits < non_zeros):
        return []

    elif non_zeros == 0 or (ok_zero_digits == available_zero_digits):
        return permutations(digit_set, total_count)

    elif zeros_ok == 0:
        return permutations(non_zero_digits, total_count)

    else:
        positions_list = list(range(non_zeros, total_count))
        return chain(
            permutations(non_zero_digits, total_count),
            map(
                lambda iters: iters[0][: iters[1]] + (0,) + iters[0][iters[1] :],
                product(permutations(non_zero_digits, total_count - 1), positions_list),
            ),
        )


def check_rec(eqparams, trace_combo=({}, 0, set(range(10))), power=0):
    max_digit_rank, multipliers_chars, non_zero_chars, zero_chars, unique_chars = (
        eqparams
    )
    prev_digits, carry_over, remaining_digits = trace_combo

    if power == max_digit_rank:
        return prev_digits if carry_over == 0 else {}

    digit_letters = unique_chars[power]
    part_sum = carry_over
    remaining_exp = []

    for first, second in multipliers_chars[power]:
        if first in prev_digits:
            part_sum += second * prev_digits[first]
        else:
            remaining_exp.append((first, second))

    for newdigs in dig_perms(
        remaining_digits, non_zero_chars[power], zero_chars[power]
    ):
        new_dict = {key: value for key, value in zip(digit_letters, newdigs)}
        testsum = part_sum + sum(
            [new_dict[first] * second for first, second in remaining_exp]
        )

        dividend, divisor = divmod(testsum, 10)

        if divisor == 0:
            new_dict.update(prev_digits)
            recurring_test = check_rec(
                eqparams,
                (new_dict, dividend, remaining_digits - set(newdigs)),
                power + 1,
            )

            if recurring_test and len(recurring_test) > 0:
                return recurring_test
    return None


def solve(puzzle):
    full_exp = [
        list(map(lambda idx: list(reversed(idx.strip())), letters.split("+")))
        for letters in puzzle.strip().upper().split("==")
    ]

    max_digit_rank = max([len(letter) for letters in full_exp for letter in letters])
    nzchars = {letter[-1] for letters in full_exp for letter in letters}
    non_zero_chars = []  # non-zero letters unique at level
    zero_chars = []  # zero-allowed letters unique at level
    unique_chars = []  # all letters unique at level
    multipliers_chars = []  # all letter with multipliers per level

    for _ in range(max_digit_rank):
        multipliers_chars.append({})
        non_zero_chars.append(set())
        zero_chars.append(set())

    for idx, letters in enumerate(full_exp):
        shifted = 1 - (idx << 1)
        for letter in letters:
            for third, forth in enumerate(letter):
                if forth not in multipliers_chars[third]:
                    multipliers_chars[third][forth] = 0
                multipliers_chars[third][forth] += shifted

    total_chars = set()

    for third, chardict in enumerate(multipliers_chars):
        for first, cnt in tuple(chardict.items()):
            if cnt == 0:  # if the cumulative is 0
                del chardict[first]

            elif first not in total_chars:
                non_zero_chars[third].add(first) if first in nzchars else zero_chars[
                    third
                ].add(first)
                total_chars.add(first)

        unique_chars.append(tuple(non_zero_chars[third]) + tuple(zero_chars[third]))
        multipliers_chars[third] = tuple(chardict.items())

    if ans := check_rec(
        [max_digit_rank, multipliers_chars, non_zero_chars, zero_chars, unique_chars]
    ):
        # sleep(0.7)
        return ans
