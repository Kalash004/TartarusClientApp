from os import system, name

from src.utils.SingletonMeta import SingletonMeta


class InputOutput(metaclass=SingletonMeta):
    def __init__(self):
        pass

    @staticmethod
    def display_start():
        welcome_string = ("Dear client, welcome to this humble, small application. \n\r"
                          "It has an ability to work with ProjectTartarus - my final project for SPSE Jecna. \n\r"
                          "Made by Anton Kalashnikov")
        print(welcome_string)

    def display_and_obtain_choices(self, to_choose_from: [str]) -> str:
        finish_str = "Please choose using numbers: "

        for i, choice in enumerate(to_choose_from):
            print(f'{i + 1}. {choice}\r')
        try:
            choice = input(finish_str)
            choice = int(choice) - 1
            choice = list(to_choose_from)[choice]
            return choice
        except Exception:
            self.clear()
            raise

    @staticmethod
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    @staticmethod
    def display_error(error_msg):
        # TODO: Add red coloring
        print(f"An error happened: {error_msg}")

    def display_tables(self, to_display, table_name):
        showing_str = "Showing data in table"
        empty_res = "Empty"
        self.clear()
        print(f"{showing_str}: {table_name}")
        if len(to_display) < 1:
            print(empty_res + "\n")
            return
        for instance in to_display:
            self.display_item(instance)

    @staticmethod
    def display_item(item):
        print(f"{item}\r")

    @staticmethod
    def display_message(msg):
        print(msg)

    @staticmethod
    def ask(msg):
        return input(msg)
