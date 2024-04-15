import json


class Parsed:
    def __init__(self, data: dict[str:str]):
        self.data = data

    def get_data(self):
        if "data" not in self.data.keys():
            return None
        if self.data["data"].lower() == "none":
            return None
        list_data = json.loads(self.data["data"])
        for d in list_data:
            d.pop("table")
        return list_data

    def get_status(self):
        return self.data["status"]
