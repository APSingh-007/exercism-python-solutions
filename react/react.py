from typing import Callable


class InputCell:
    def __init__(self, initial_value: int) -> None:
        self._value = initial_value
        self.dependents: set[InputCell, ComputeCell] = set()
        self.change_counter = 0

    def add_dependent(self, cell: object) -> None:
        self.dependents.add(cell)

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        if self._value != value:
            self._value = value
            self.change_counter += 1
            for cell in self.dependents:
                cell.recompute()


class ComputeCell(InputCell):
    def __init__(self, inputs: list[InputCell], compute_function: Callable) -> None:
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks: set[Callable] = set()

        for inp in inputs:
            inp.add_dependent(self)
        super().__init__(self.compute())

    def compute(self) -> int:
        return self.compute_function([cell.value for cell in self.inputs])

    def recompute(self) -> None:
        if len(set([cell.change_counter for cell in self.inputs])) != 1:
            return
        new_value: int = self.compute()
        if new_value != self.value:
            self.value = new_value
            for cb in self.callbacks:
                cb(self.value)

    def add_callback(self, callback: Callable) -> None:
        self.callbacks.add(callback)

    def remove_callback(self, callback: Callable) -> None:
        if callback in self.callbacks:
            self.callbacks.remove(callback)
