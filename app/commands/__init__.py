from abc import ABC, abstractmethod
import logging

class Command(ABC):
    @abstractmethod
    def execute(self, args):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command
        logging.info(f"Registered command: {command_name}")

    def execute_command(self, command_name: str, args):
       try:
           logging.info(f"Executing command: {command_name} with args: {args}")
           self.commands[command_name].execute(args)
       except KeyError:
           logging.info(f"No such command: {command_name}")
           print(f"No such command: {command_name}")

