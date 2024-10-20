from decimal import Decimal, InvalidOperation
from app.commands import Command
from app.calculator import Calculator

class AddCommand(Command):
    def execute(self, args):
        if len(args) != 2:
            print("Usage: add <number1> <number2>")
            return "Usage: add <number1> <number2>"
            
        try:
            num1 = Decimal(args[0])
            num2 = Decimal(args[1])
            result = Calculator.add(num1, num2)
            print(result)
            return result
        except InvalidOperation:
            print("Invalid number format")
            return "Invalid number format"