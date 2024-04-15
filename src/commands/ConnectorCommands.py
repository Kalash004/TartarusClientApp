import abc

from src.layers.Connector import Connector

con = Connector()


class ICommand:

    @abc.abstractmethod
    def execute(self):
        raise NotImplemented


class DeleteById(ICommand):
    def __init__(self, row_id: int, table):
        self.row_id = row_id
        self.table = table

    def execute(self):
        return con.delete(self.table, self.row_id)


class GetAll(ICommand):
    def __init__(self, table):
        self.table = table

    def execute(self):
        return con.get_all(self.table)


class GetWithParams(ICommand):
    def __init__(self, table, params):
        self.table = table
        self.params = params

    def execute(self):
        return con.get_params(self.table, self.params)


class Update(ICommand):
    def __init__(self, table, data):
        self.table = table
        self.data = data

    def execute(self):
        return con.update(self.table, self.data)


class Insert(ICommand):
    def __init__(self, table, data):
        self.table = table
        self.data = data

    def execute(self):
        return con.post(self.table, self.data)
