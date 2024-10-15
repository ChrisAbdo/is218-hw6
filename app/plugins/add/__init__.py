from app.commands import Command

class AddCommand(Command):
    def execute(self):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 + num2
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")