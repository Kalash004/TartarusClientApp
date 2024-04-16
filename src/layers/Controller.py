import traceback

from src.AnswerParser import AnswerParser
from src.commands.InputOutputCommands import DisplayError, DisplayMenu, DisplayMessage, Clear, Start, DisplayData, Ask
from src.logger.MyLogger import MyLogger
from src.models.ActionTable import ActionTable
from src.utils.SingletonMeta import SingletonMeta


class Controller(metaclass=SingletonMeta):
    def __init__(self):
        self.stop = False
        self.table_menu = {
            "Admin users": ActionTable("admin_users", self.post_request_data_admin_users, self.update_request_data_admin_users),
            "Office users": ActionTable("office_users", self.post_request_data_office_users, self.update_request_data_office_users),
            "Days": ActionTable("days", self.not_implemeneted, self.not_implemeneted),
            "System messages": ActionTable("system_messages", self.not_implemeneted, self.not_implemeneted),
            "System logins": ActionTable("system_log_ins", self.not_implemeneted, self.not_implemeneted),
            "Enterences to office": ActionTable("enterences_to_office", self.not_implemeneted, self.not_implemeneted)
        }

    def start(self):
        Start().execute()
        self.loop()

    def loop(self):
        while not self.stop:
            try:
                table = self.display_table_menu(self.table_menu, "Table menu")
                action_table: ActionTable = self.table_menu[table]
                action = self.display_table_menu(action_table.action_menu, "Action menu")
                resp: bytes = action_table.action(action)
                parsed = AnswerParser.parse(resp.decode())
                status = parsed.get_status()
                data_list = parsed.get_data()
                DisplayMessage(f"Answer from core app:\n"
                               f"Status:{status}").execute()
                if data_list is not None:
                    DisplayData(data_list, table).execute()
            except Exception as e:
                tb = traceback.format_exc()
                MyLogger().log_exception(e, tb)
                DisplayError(e).execute()

    @staticmethod
    def display_table_menu(menu, message):
        DisplayMessage(message).execute()
        choice = DisplayMenu(menu).execute()
        Clear().execute()
        return choice

    @staticmethod
    def post_request_data_admin_users():
        Clear().execute()
        isntance_id = None
        name = Ask("Please write name of the user: ").execute()
        surename = Ask("Please write surename of the user: ").execute()
        password = Ask("Please write password of the user: ").execute()
        data = f"{{admin_id:none,name:{name},surename:{surename},password:{password}}}"
        print(data)
        return data

    @staticmethod
    def update_request_data_admin_users():
        instance_id = Ask("Please enter id of the instance you want to update: ").execute()
        name = Ask("Please write name of the user: ").execute()
        surename = Ask("Please write surename of the user: ").execute()
        password = Ask("Please write password of the user: ").execute()
        data = f"{{admin_id:{instance_id},name:{name},surename:{surename},password:{password}}}"
        return data

    @staticmethod
    def update_request_data_office_users():
        instance_id = Ask("Please enter id of the instance you want to update: ").execute()
        name = Ask("Please write name of the user: ").execute()
        surename = Ask("Please write surename of the user: ").execute()
        password = Ask("Please write password of the user: ").execute()
        data = f"{{users_id:{instance_id},name:{name},surename:{surename},password:{password}}}"
        return data

    @staticmethod
    def post_request_data_office_users():
        # TODO: Ask for ID/NONE, name, surename, password
        Clear().execute()
        isntance_id = None
        name = Ask("Please write name of the user: ").execute()
        surename = Ask("Please write surename of the user: ").execute()
        password = Ask("Please write password of the user: ").execute()
        data = f"{{users_id:none,name:{name},surename:{surename},password:{password}}}"
        print(data)
        return data

    def not_implemeneted(self):
        raise NotImplemented
