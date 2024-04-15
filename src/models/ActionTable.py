from src.commands.ConnectorCommands import GetWithParams, GetAll, DeleteById, Insert, Update
from src.commands.InputOutputCommands import Clear, GetParameters, Ask


class ActionTable:
    def __init__(self, table_name, post_data_requester, update_data_requester):
        self.table_name = table_name
        self.post_data_req = post_data_requester
        self.update_data_req = update_data_requester
        self.action_menu = {
            "See all data": self.get_all_request,
            "See using parameters": self.get_with_params_request,
            "Delete": self.delete_by_id,
            "Insert": self.insert,
            "Update": self.update
        }

    def action(self, action: str):
        return self.action_menu[action](self.table_name)

    @staticmethod
    def get_with_params_request(table):
        Clear().execute()
        params: dict[str:str] = GetParameters().execute()
        resp = GetWithParams(table, params).execute()
        return resp

    @staticmethod
    def get_all_request(table):
        Clear().execute()
        resp = GetAll(table).execute()
        return resp

    @staticmethod
    def delete_by_id(table):
        Clear().execute()
        row_id = int(Ask("Please give me and id of the row you want to delete: ").execute())
        resp = DeleteById(row_id, table).execute()
        return resp

    def insert(self, table):
        data = self.post_data_req()
        Clear().execute()
        resp = Insert(table, data).execute()
        return resp

    def update(self, table):
        data = self.update_data_req()
        Clear().execute()
        resp = Update(table, data).execute()
        return resp
