import os

from src.utils.SingletonMeta import SingletonMeta


def read_json_file(path: str, var_name: str) -> [int | str]:
    import json
    with open(path, "r") as file:
        response = []
        data = json.load(file)
        if type(data[var_name]) is list:
            for i in data[var_name]:
                response.append(i)
            return response
        response = [data[var_name]]
        return response


class AuthLoader(metaclass=SingletonMeta):
    def __init__(self, path):
        self.FILE_PATH = path
        self.__API_KEYS_VAR_NAME = "apikey"

    def get_auth_api_keys(self) -> str:
        return read_json_file(self.FILE_PATH, self.__API_KEYS_VAR_NAME)[0]


class ApiLoader:
    def __init__(self, path):
        self.FILE_PATH = path

    def get_port(self) -> int:
        return read_json_file(self.FILE_PATH, "api_server_running_port")[0]

    def get_host(self) -> str:
        return read_json_file(self.FILE_PATH, "api_server_running_host")[0]


class ConfigLoader(metaclass=SingletonMeta):
    """This loads parameters from config files"""

    def __init__(self):
        self.__AUTHENTIFICATOR_CONF_FILE_PATH = os.path.join(os.path.dirname(__file__), "../../config/apikey_conf.json")
        self.__API_SERVER_FILE_PATH = os.path.join(os.path.dirname(__file__), "../../config/connection_conf.json")

        self.auth_conf_loader = AuthLoader(self.__AUTHENTIFICATOR_CONF_FILE_PATH)
        self.api_conf_loader = ApiLoader(self.__API_SERVER_FILE_PATH)
