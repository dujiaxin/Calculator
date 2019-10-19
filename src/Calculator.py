def addition(a, b):
    return a + b


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = a + b
        return addition(a, b)
