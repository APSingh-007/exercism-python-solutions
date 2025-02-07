from dataclasses import dataclass
from collections import defaultdict

RESULT = {
    "win": ((1, 0, 0), (0, 0, 1)),
    "draw": ((0, 1, 0), (0, 1, 0)),
    "loss": ((0, 0, 1), (1, 0, 0)),
}


@dataclass
class Team:
    wins: int = 0
    loss: int = 0
    draw: int = 0

    @property
    def matches(self):
        return self.wins + self.loss + self.draw

    @property
    def points(self):
        return self.wins * 3 + self.draw


def tally(rows: list[str]) -> list[str]:
    match_data = [row.split(";") for row in rows]
    scoreboard = defaultdict(Team)
    answer = [
        f"{'Team':<30} | MP |  W |  D |  L |  P",
    ]

    for row in match_data:
        if len(row) != 3:
            raise ValueError("Invalid Input Data")

        team1, team2, res = row
        try:
            ((t1_w, t1_d, t1_l), (t2_w, t2_d, t2_l)) = RESULT[res]
        except KeyError:
            raise KeyError("Invalid Match Result Data")

        scoreboard[team1].wins += t1_w
        scoreboard[team1].draw += t1_d
        scoreboard[team1].loss += t1_l
        scoreboard[team2].wins += t2_w
        scoreboard[team2].draw += t2_d
        scoreboard[team2].loss += t2_l

    for name, board in sorted(
        scoreboard.items(), key=lambda row: (-row[1].points, row[0])
    ):
        answer.append(
            f"{name:<30} |{board.matches:>3} |{board.wins:>3} |{board.draw:>3} |{board.loss:>3} |{board.points:>3}"
        )

    return answer
