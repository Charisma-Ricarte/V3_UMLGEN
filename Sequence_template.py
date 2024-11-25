class Calculator:
    def add(self, a, b):
        return a + b

class User:
    def perform_calculation(self):
        calc = Calculator()
        result = calc.add(3, 5)
        print(f"Result is {result}")

user = User()
user.perform_calculation()
