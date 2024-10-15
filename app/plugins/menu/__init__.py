from app.commands import Command

class MenuCommand(Command):
    def execute(self):
        print("\nAvailable commands:")
        print("- add")
        print("- subtract")
        print("- multiply")
        print("- divide")
        print("- menu (display this menu)")
        print("- exit (quit the application)")