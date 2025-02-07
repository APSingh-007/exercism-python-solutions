class CustomSet:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = []

        for item in elements:
            self.add(item)

    def isempty(self):
        return not bool(self.elements)

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        for item in self.elements:
            if item not in other.elements:
                return False
        return True

    def isdisjoint(self, other):
        return self.intersection(other).isempty()

    def __eq__(self, other) -> bool:
        if len(self.elements) != len(other.elements):
            return False
        return self.issubset(other)

    def add(self, item) -> None:
        if item in self.elements:
            return
        self.elements.append(item)

    def intersection(self, other):
        intersection = CustomSet()
        for item in other.elements:
            if item in self.elements:
                intersection.add(item=item)
        return intersection

    def __sub__(self, other):
        result = CustomSet()
        for item in self.elements:
            if item not in other.elements:
                result.add(item=item)
        return result

    def __add__(self, other):
        result = CustomSet()
        for item in self.elements + other.elements:
            result.add(item=item)
        return result
