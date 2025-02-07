class Rational:
    def __init__(self, numer, denom):
        def compute_hcf(num1, num2):
            # HCF found using euclidean rule
            while num2:
                num1, num2 = num2, num1 % num2
            return num1

        hcf = abs(compute_hcf(numer, denom))
        if denom < 0:
            numer *= -1
            denom *= -1
        self.numer = numer // hcf
        self.denom = denom // hcf

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f"Rational(numer='{self.numer}', denom='{self.denom}')"

    def __str__(self):
        return f"{self.numer}/{self.denom}"

    def __add__(self, other):
        numer = self.numer * other.denom + self.denom * other.numer
        denom = self.denom * other.denom
        return Rational(numer=numer, denom=denom)

    def __sub__(self, other):
        numer = self.numer * other.denom - self.denom * other.numer
        denom = self.denom * other.denom
        return Rational(numer=numer, denom=denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer=numer, denom=denom)

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        return Rational(numer=numer, denom=denom)

    def __abs__(self):
        return Rational(numer=abs(self.numer), denom=abs(self.denom))

    def __pow__(self, power):
        numer = self.numer ** abs(power)
        denom = self.denom ** abs(power)
        if power < 0:
            numer, denom = denom, numer
        return Rational(numer=numer, denom=denom)

    def __rpow__(self, base):
        """Exponentiation of a real number, to a Rational Number, x^(a/b) = root(x^a, b), where root(p, q) is the qth root of p. In other words,  p ** (1/q) where, p = x ** a"""

        return (base**self.numer) ** (1 / self.denom)


# Optimised by ChatGPT
"""
import math

class Rational:
    def __init__(self, numer, denom):
        if denom == 0:
            raise ValueError("Denominator cannot be zero.")
        
        hcf = abs(math.gcd(numer, denom))  # Use built-in gcd for efficiency
        if denom < 0:
            numer, denom = -numer, -denom
        self.numer = numer // hcf
        self.denom = denom // hcf

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numer == other.numer and self.denom == other.denom
        return False

    def __repr__(self):
        return f"Rational(numer={self.numer}, denom={self.denom})"

    def __str__(self):
        return f"{self.numer}/{self.denom}"

    def __add__(self, other):
        if isinstance(other, Rational):
            numer = self.numer * other.denom + other.numer * self.denom
            denom = self.denom * other.denom
            return Rational(numer, denom)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Rational):
            numer = self.numer * other.denom - other.numer * self.denom
            denom = self.denom * other.denom
            return Rational(numer, denom)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numer * other.numer, self.denom * other.denom)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numer * other.denom, self.denom * other.numer)
        return NotImplemented

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        numer = self.numer ** abs(power)
        denom = self.denom ** abs(power)
        if power < 0:
            numer, denom = denom, numer
        return Rational(numer, denom)

    def __rpow__(self, base):
        return (base**self.numer) ** (1 / self.denom)
"""


obj = Rational(31, 3)
print(obj.__repr__())
print(obj)
