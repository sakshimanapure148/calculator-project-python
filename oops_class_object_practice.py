"""Beginner OOP practice: classes, objects, attributes, and methods."""


class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def display(self):
        print(f"Laptop brand: {self.brand}")
        print(f"RAM: {self.ram} GB")


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2


if __name__ == "__main__":
    print("=== Laptop Class ===")
    laptop1 = Laptop("Dell", 16)
    laptop1.display()

    print("\n=== Calculator Class ===")
    calculator = Calculator(20, 5)
    print(f"Addition: {calculator.add()}")
    print(f"Subtraction: {calculator.subtract()}")
    print(f"Multiplication: {calculator.multiply()}")
