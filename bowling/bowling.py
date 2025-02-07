TYPES = ["strike", "spare", "open-frame"]


class Frame:
    def __init__(self, pins: int) -> None:
        self.throws: list[int] = [pins]
        self.type: str = ""
        self.frame_score: int = 0

    def __repr__(self) -> str:
        return f"Frame: ( {self.throws}, {self.type}, {self.frame_score} )"


class BowlingGame:
    def __init__(self) -> None:
        self.first_throw: int = True
        self.frames: list[Frame] = []
        self.frames_count: int = 0
        self.bonus_rolls: int = 0
        self.total_score: int = 0

    def roll(self, pins: int) -> None:
        if not (0 <= pins <= 10):
            raise ValueError("Invalid number of pins for a throw")

        if self.frames_count == 10:
            self.bonus_rolls += 1
            tenth_frame = self.frames[9]
            if (
                (tenth_frame.type == TYPES[0] and self.bonus_rolls > 2)
                or (tenth_frame.type == TYPES[1] and self.bonus_rolls > 1)
                or (tenth_frame.type == TYPES[2] and self.bonus_rolls > 0)
            ):
                raise ValueError("Cannot roll after bonus rolls... Invalid roll")

        if self.first_throw:
            new_frame = Frame(pins)
            if pins == 10:
                new_frame.type = TYPES[0]
                self.frames_count += 1 if self.frames_count < 10 else 0
                self.frames.append(new_frame)
                return
            self.frames.append(new_frame)
            self.first_throw = False
        else:
            current_frame = self.frames[-1]
            current_frame.throws.append(pins)
            self.frames_count += 1 if self.frames_count < 10 else 0
            self.first_throw = True
            pins_in_frame = sum(current_frame.throws)

            if pins_in_frame == 10:
                current_frame.type = TYPES[1]
            elif pins_in_frame < 10:
                current_frame.type = TYPES[2]
            else:
                raise ValueError("Any frame cannot have more than 10 knocked pins")

    def score(self):
        if self.frames_count < 10:
            raise ValueError("The game is still Incomplete.")

        for index in range(10):
            frame: Frame = self.frames[index]

            if frame.type == TYPES[2]:
                frame.frame_score = sum(frame.throws)
            elif frame.type == TYPES[1]:
                next_throw: int = self.frames[index + 1].throws[0]
                frame.frame_score = 10 + next_throw
            else:
                next_throw: int = self.frames[index + 1].throws[0]
                second_next_throw: int = (
                    self.frames[index + 2].throws[0]
                    if next_throw == 10
                    else self.frames[index + 1].throws[1]
                )
                frame.frame_score = 10 + next_throw + second_next_throw

            self.total_score += frame.frame_score

        return self.total_score
