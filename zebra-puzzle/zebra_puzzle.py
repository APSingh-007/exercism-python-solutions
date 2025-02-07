from itertools import permutations as perms


def solve() -> tuple[str, str]:
    for englishman, spaniard, ukrainian, norwegian, japanese in perms(range(1, 6)):
        if norwegian == 1:
            for coffee, tea, milk, orange_juice, water in perms(range(1, 6)):
                if milk == 3 and ukrainian == tea:
                    for blue, red, green, ivory, yellow in perms(range(1, 6)):
                        if (
                            green == ivory + 1
                            and blue == norwegian + 1
                            and englishman == red
                            and green == coffee
                        ):
                            for dog, horse, snail, fox, zebra in perms(range(1, 6)):
                                if spaniard == dog:
                                    for (
                                        painting,
                                        chess,
                                        dancing,
                                        reading,
                                        football,
                                    ) in perms(range(1, 6)):
                                        if (
                                            snail == dancing
                                            and yellow == painting
                                            and japanese == chess
                                            and football == orange_juice
                                            and abs(reading - fox) == 1
                                            and abs(painting - horse) == 1
                                        ):
                                            nationalities: dict = {
                                                englishman: "Englishman",
                                                japanese: "Japanese",
                                                ukrainian: "Ukrainian",
                                                norwegian: "Norwegian",
                                                spaniard: "Spaniard",
                                            }

                                            return (
                                                nationalities[water],
                                                nationalities[zebra],
                                            )

                                            """
                                            Below (Commented out code) is to print the table as solved
                                            """

                                            # drink = {
                                            #     coffee: "coffee",
                                            #     tea: "tea",
                                            #     milk: "milk",
                                            #     orange_juice: "orange_juice",
                                            #     water: "water",
                                            # }

                                            # colour = {
                                            #     blue: "blue",
                                            #     red: "red",
                                            #     green: "green",
                                            #     ivory: "ivory",
                                            #     yellow: "yellow",
                                            # }

                                            # pet = {
                                            #     dog: "dog",
                                            #     horse: "horse",
                                            #     snail: "snail",
                                            #     fox: "fox",
                                            #     zebra: "zebra",
                                            # }

                                            # hobby = {
                                            #     painting: "painting",
                                            #     chess: "chess",
                                            #     dancing: "dancing",
                                            #     reading: "reading",
                                            #     football: "football",
                                            # }

                                            # properties = (
                                            #     nationalities,
                                            #     drink,
                                            #     colour,
                                            #     pet,
                                            #     hobby,
                                            # )

                                            # sep = "|"
                                            # answer = f"H0{sep :>11} H1{sep :>11} H2{sep :>11} H3{sep :>11} H4{sep :>11}"

                                            # for prop in properties:
                                            #     data = "| ".join(
                                            #         f"{str(prop[i]) :<12}"
                                            #         for i in range(1, 6)
                                            #     )
                                            #     answer += "\n" + data + sep
                                            # return answer


ANSWER = solve()


def drinks_water():
    return ANSWER[0]


def owns_zebra():
    return ANSWER[1]
