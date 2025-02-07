PLANTS = {
    "R": "Radishes",
    "V": "Violets",
    "C": "Clover",
    "G": "Grass",
}
DEFAULT_STUDENTS = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
    "Kincaid",
    "Larry",
]


class Garden:
    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.diagram = diagram
        self.students = sorted(students)
        self.data = self.assign_plants()

    def assign_plants(self) -> None:
        data = {}
        top_shelf, bot_self = self.diagram.split("\n")

        for i, student in enumerate(self.students):
            plant_initials = top_shelf[i * 2 : i * 2 + 2] + bot_self[i * 2 : i * 2 + 2]
            data[student] = [PLANTS[plant] for plant in plant_initials]

        return data

    def plants(self, name: str) -> list:
        return self.data[name]
