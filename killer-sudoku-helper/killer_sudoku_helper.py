NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def combinations(
    target_sum: int, cage_size: int, excluded_digits: list[int]
) -> list[int]:
    result: list[list[int]] = []

    def backtrack(res: list, shelf: list):
        if len(res) < cage_size and shelf:
            for i, num in enumerate(shelf):
                backtrack([*res, num], shelf[i + 1 :])
        if len(res) == cage_size and sum(res) == target_sum:
            result.append(res)

    backtrack([], [i for i in NUMS if i not in excluded_digits])

    return result


"""
From Other Solutions ( Uncomment Below )
"""

# def combinations(total, n, excluded):
#     def backtrack(start, current_comb, remaining_sum):
#         # Base case: if the current combination has reached the desired length
#         if len(current_comb) == n:
#             # Check if the combination sums to the target total
#             if remaining_sum == 0:
#                 result.append(current_comb[:])
#             return

#         # Iterate over possible numbers to include in the combination
#         for i in range(start, 10):
#             # Skip numbers that are excluded or would result in an invalid combination
#             if i not in excluded and remaining_sum - i >= 0:
#                 # Include the current number and recurse
#                 current_comb.append(i)
#                 backtrack(i + 1, current_comb, remaining_sum - i)
#                 # Backtrack by removing the last added number
#                 current_comb.pop()

#     result = []
#     # Start the backtracking process
#     backtrack(1, [], total)
#     return result
