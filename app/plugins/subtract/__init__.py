from decimal import Decimal, InvalidOperation
from app.commands import Command
from app.calculator import Calculator

class SubtractCommand(Command):
    def execute(self, args):
        try:
            num1 = Decimal(args[0])
            num2 = Decimal(args[1])
            result = Calculator.subtract(num1, num2)
            print(f"Result: {result}")
        except InvalidOperation:
            print("Invalid input. Please enter numeric values.")