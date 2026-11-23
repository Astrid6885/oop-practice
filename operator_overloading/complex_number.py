"""Problem 1 - Complex numbers: overload + and -."""


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real  # real part
        self.imag = imag  # imaginary part

    def __add__(self, other):
        # (a + bi) + (c + di) = (a + c) + (b + d)i
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        # (a + bi) - (c + di) = (a - c) + (b - d)i
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __eq__(self, other):
        # Useful to compare results in the tests
        return self.real == other.real and self.imag == other.imag

    def __str__(self):
        # Nice display, e.g. "3 + 2i" or "3 - 2i"
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"


if __name__ == "__main__":
    z1 = ComplexNumber(3, 2)
    z2 = ComplexNumber(1, 7)
    print("z1 =", z1)
    print("z2 =", z2)
    print("z1 + z2 =", z1 + z2)  # 4 + 9i
    print("z1 - z2 =", z1 - z2)  # 2 - 5i
