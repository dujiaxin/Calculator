def addition(a, b):
    a = int(a)
    b = int(b)
    return a + b


def subtraction(substract, substracted):
    substract = int(substract)
    substracted = int(substracted)
    return substracted - substract


def multiply(a, b):
    a = int(a)
    b = int(b)
    return a * b

def division(a, b):
    a = int(a)
    b = int(b)
    return round(b / a, 9)

def square(a):
    a = int(a)
    return a * a

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiplication(self, a, b):
        self.result = multiply(a, b)
        return self.result

    def division(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result