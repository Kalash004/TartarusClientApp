# "b'\n\rSTATUS:1;DATA:[{"table": "admin_users", "admin_id": 4, "name": "Anton", "surename": "Kalashnikov", "password": "test"}, {"table": "admin_users", "admin_id": 5, "name": "Someone", "surename": "Kalashnikov", "password": "newpas"}, {"table": "admin_users", "admin_id": 6, "name": "Notna", "surename": "Kalashnikov", "password": "test"}, {"table": "admin_users", "admin_id": 7, "name": "Notna", "surename": "Kalashnikov", "password": "test"}, {"table": "admin_users", "admin_id": 9, "name": "Denis", "surename": "Kalashnikov", "password": "test"}]'"
from src.models.Parsed import Parsed


class AnswerParser:

    @staticmethod
    def parse(data: str):
        data = data.lstrip("\n\r")
        data = data.rstrip(";")
        parts = data.split(";")
        parsed = {}
        for part in parts:
            part = part.split(":", 1)
            key = part[0].lower()
            value = part[1]
            parsed[key] = value
        return Parsed(parsed)
