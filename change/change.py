def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    # Sort the coins denomination
    coins.sort()

    # Memoization
    memo: list[tuple] = [(0, [])]

    if target < 0:
        raise ValueError("target can't be negative")

    for total in range(1, target + 1):
        coin_count = 0
        possible: bool = False

        for coin in coins:
            if coin > total:
                break

            remains: int = total - coin

            if remains == 0:
                coin_count = 1
                coin_list = [coin]
                possible = True
                break

            memo_tup = memo[remains]

            if not memo_tup:
                continue

            if coin_count == 0 or (memo_tup[0] + 1) < coin_count:
                coin_count = memo_tup[0] + 1
                coin_list = [coin] + memo_tup[1]
                possible = True

        if possible:
            memo.append((coin_count, coin_list))
        else:
            memo.append(False)

    if not memo[target]:
        raise ValueError("can't make target with given coins")

    return memo[target][1]
