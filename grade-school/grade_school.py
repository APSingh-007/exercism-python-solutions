class School:
    def __init__(self):
        self.grades_dict = {}
        self.add = []

    def add_student(self, name, grade):
        if name not in self.roster():
            self.grades_dict[grade] = self.grades_dict.get(grade, []) + [name]
            self.add.append(True)
        else:
            self.add.append(False)

    def roster(self):
        result = []
        for grade in sorted(self.grades_dict.keys()):
            result += self.grade(grade)
        return result

    def grade(self, grade_number):
        return sorted(self.grades_dict.get(grade_number, []))

    def added(self):
        return self.add
