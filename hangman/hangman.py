# Game status categories
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word: str) -> None:
        self.word: str = word
        self.correctly_guessed: set[int] = set()
        self.remaining_guesses: int = 9
        self.status: str = STATUS_ONGOING

    def guess(self, char: str) -> None:
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")

        if char in self.word and char not in self.correctly_guessed:
            self.correctly_guessed.add(char)
        else:
            self.remaining_guesses -= 1

        if set(self.word) == self.correctly_guessed:
            self.status = STATUS_WIN
        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE

    def get_masked_word(self) -> str:
        return "".join(
            [char if char in self.correctly_guessed else "_" for char in self.word]
        )

    def get_status(self) -> str:
        return self.status
