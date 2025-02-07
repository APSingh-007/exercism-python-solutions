class Clock:
    def __init__(self, hour: int, minute: int) -> None:
        self.hour = (hour + (minute // 60)) % 24
        self.minute = minute % 60

    def __repr__(self) -> str:
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self) -> str:
        hrs = str(self.hour).rjust(2, "0")
        mins = str(self.minute).rjust(2, "0")
        return f"{hrs}:{mins}"

    def __eq__(self, other) -> bool:
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes: int):
        self.hour = (self.hour + (self.minute + minutes) // 60) % 24
        self.minute = (self.minute + minutes) % 60
        return self

    def __sub__(self, minutes: int):
        mins = self.hour * 60 + self.minute - minutes
        self.hour = (mins // 60) % 24
        self.minute = mins % 60
        return self
