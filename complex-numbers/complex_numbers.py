from math import e, sin, cos


class ComplexNumber:
    def __init__(self, real, imaginary) -> None:
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other) -> bool:
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other) -> "ComplexNumber":
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real + other, self.imaginary)

        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)

    def __radd__(self, other) -> "ComplexNumber":
        return self + other

    def __sub__(self, other) -> "ComplexNumber":
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real - other, self.imaginary)

        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return ComplexNumber(real, imaginary)

    def __rsub__(self, other) -> "ComplexNumber":
        return -1 * self + other

    def __mul__(self, other) -> "ComplexNumber":
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real * other, self.imaginary * other)

        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)

    def __rmul__(self, other) -> "ComplexNumber":
        return self * other

    def __truediv__(self, other) -> "ComplexNumber":
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real / other, self.imaginary / other)
        denominator = other.real**2 + other.imaginary**2
        numerator_real = self.real * other.real + self.imaginary * other.imaginary
        numerator_imaginary = other.real * self.imaginary - self.real * other.imaginary
        return ComplexNumber(
            numerator_real / denominator, numerator_imaginary / denominator
        )

    def __rtruediv__(self, other) -> "ComplexNumber":
        return ComplexNumber(other, 0) / self

    def __abs__(self) -> "ComplexNumber":
        return (self.real**2 + self.imaginary**2) ** 0.5

    def conjugate(self) -> "ComplexNumber":
        return ComplexNumber(self.real, -1 * self.imaginary)

    def exp(self) -> "ComplexNumber":
        first = e**self.real
        second = cos(self.imaginary) + (ComplexNumber(0, 1) * sin(self.imaginary))
        return first * second
