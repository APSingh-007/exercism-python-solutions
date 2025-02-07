VALUES = "**234567891JQKA"


def best_hands(hands: list) -> list:
    result: dict = {
        "highest_cards": [],
        "cards_values": [],
        "rank": 0,
    }

    for hand in hands:
        rank: int = 0  # higher number of rank means stronger hand
        cards: list = [VALUES.index(card[0]) for card in hand.split()]
        suits: list = [card[-1] for card in hand.split()]

        groups: list = sorted(
            {(cards.count(card), card) for card in cards},
            reverse=True,
        )

        is_straight, cards = check_straight(cards)
        is_flush: bool = len(set(suits)) == 1

        card_counts: list = [count for count, _ in groups]
        # If frequency is same, the line below sorts by card Value
        cards_in_dec_freq: list = cards if is_straight else [card for _, card in groups]
        print(cards_in_dec_freq)

        if is_straight and is_flush:
            rank = 9
        elif card_counts == [4, 1]:
            rank = 8
        elif card_counts == [3, 2]:
            rank = 7
        elif is_flush:
            rank = 6
        elif is_straight:
            rank = 5
        elif card_counts == [3, 1, 1]:
            rank = 4
        elif card_counts == [2, 2, 1]:
            rank = 3
        elif card_counts == [2, 1, 1, 1]:
            rank = 2
        else:
            rank = 1

        if rank >= result["rank"]:
            # Break Ties between hands and check update highest card in result dictionary
            if (
                rank == result["rank"]
                and result["cards_values"][0] == cards_in_dec_freq
            ):
                result["highest_cards"].append(hand)
                result["cards_values"].append(cards_in_dec_freq)

            elif rank > result["rank"] or (
                rank == result["rank"] and result["cards_values"][0] < cards_in_dec_freq
            ):
                result["highest_cards"] = [hand]
                result["cards_values"] = [cards_in_dec_freq]
                result["rank"] = rank

    return result["highest_cards"]


def check_straight(hand: list) -> bool:
    # We can use Ace = 1 in case of a 5 high straight
    hand.sort(reverse=True)
    if hand == [14, 5, 4, 3, 2]:
        hand = [5, 4, 3, 2, 1]
    return len(set(hand)) == 5 and hand[0] - hand[-1] == 4, hand
