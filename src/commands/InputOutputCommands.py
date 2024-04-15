import abc

from src.layers.InputOutput import InputOutput

io = InputOutput()


class ICommand:

    @abc.abstractmethod
    def execute(self):
        raise NotImplemented


class Start(ICommand):

    def execute(self):
        io.display_start()


class DisplayMenu(ICommand):

    def __init__(self, menu):
        self.menu = menu

    def execute(self):
        return io.display_and_obtain_choices(self.menu)


class DisplayError(ICommand):
    def __init__(self, message):
        self.message = message

    def execute(self):
        io.display_error(self.message)


class DisplayMessage(ICommand):
    def __init__(self, message):
        self.message = message

    def execute(self):
        io.display_message(self.message)


class Clear(ICommand):
    def execute(self):
        io.clear()


class Ask(ICommand):
    def __init__(self, request):
        self.req = request

    def execute(self):
        answr = io.ask(self.req)
        return answr


class GetParameters(ICommand):
    def __init__(self):
        pass

    def execute(self):
        stop = False
        params = {}
        while not stop:
            param_name = Ask("Please give me an parameter name: ").execute()
            value = Ask("Please tell me what should it equel to: ").execute()
            params[param_name] = value
            to_stop: str = Ask("Is that enough ? Press y to stop: ").execute()
            if to_stop.lower() == "y":
                stop = True
        return params


class DisplayData(ICommand):
    def __init__(self, data_list, table_name):
        self.data_list = data_list
        self.table_name = table_name

    def execute(self):
        io.display_tables(self.data_list, self.table_name)
