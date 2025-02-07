class HighScores:
    def __init__(self, scores: list):
        self.scores = scores
        self.sorted_scores = sorted(scores, reverse=True)

    def personal_best(self) -> int:
        return self.sorted_scores[0]

    def personal_top_three(self) -> int:
        return self.sorted_scores[:3]

    def latest(self) -> int:
        return self.scores[-1]
