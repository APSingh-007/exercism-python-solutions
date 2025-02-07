def tally(rows: list[str]) -> list[str]:
    table: dict[str : dict[str:int]] = {}
    answer = [
        f"{'Team'.ljust(30)} | MP |  W |  D |  L |  P",
    ]

    for row in rows:
        *teams, res = row.split(";")
        result = [(0, 1, 0), (0, 1, 0)]  # (win, draw, loss)
        if res == "win":
            result = [(1, 0, 0), (0, 0, 1)]
        if res == "loss":
            result = [(0, 0, 1), (1, 0, 0)]

        for i, team in enumerate(teams):
            if team not in table.keys():
                table[team] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}

            table[team]["MP"] += 1
            table[team]["W"] += result[i][0]
            table[team]["D"] += result[i][1]
            table[team]["L"] += result[i][2]
            table[team]["P"] += result[i][0] * 3 + result[i][1]

    for team, board in sorted(table.items(), key=lambda item: (-item[1]["P"], item[0])):
        matches = str(board["MP"]).rjust(3)
        win = str(board["W"]).rjust(3)
        draw = str(board["D"]).rjust(3)
        loss = str(board["L"]).rjust(3)
        points = str(board["P"]).rjust(3)

        row = f"{team.ljust(30)} |{matches} |{win} |{draw} |{loss} |{points}"
        answer.append(row)

    return answer
