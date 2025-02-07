# from itertools import cycle

NOTES_SHARP = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
NOTES_FLAT = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]

SHARP = ["G", "D", "A", "E", "B", "F#", "C", "e", "b", "f#", "c#", "g#", "d#", "C", "a"]
FLAT = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"]


class Scale:
    def __init__(self, tonic: str) -> None:
        self.tonic = tonic

    def chromatic(self) -> list:
        if self.tonic in SHARP:
            notes = NOTES_SHARP
        elif self.tonic in FLAT:
            notes = NOTES_FLAT
        else:
            raise ValueError("Invalid Tonic")

        start = notes.index(self.tonic.title())
        return notes[start:] + notes[:start]

    def interval(self, intervals: str):
        chromatic = self.chromatic()
        result: list = []
        index = 0

        for step in intervals:
            result.append(chromatic[index])
            index += {"m": 1, "M": 2, "A": 3}[step]
        return result + [chromatic[0]]
