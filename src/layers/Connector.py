import socket

from src.utils.SingletonMeta import SingletonMeta


class Connector(metaclass=SingletonMeta):
    def __init__(self):
        self.apikey = "apitestkey1"
        self.server_address = "127.0.0.1"
        self.server_port = 2004

    def post(self, table, data):
        request = f"APIKEY={self.apikey};EVENT=POST;TABLE={table};DATA=[{data}]"
        resp = self.send_request(request)
        return resp

    def get_all(self, table):
        request = f"APIKEY={self.apikey};EVENT=GET;TABLE={table};"
        resp = self.send_request(request)
        return resp

    def get_params(self, table, params: dict[str | str]):
        parameters = ""
        for key, val in params.items():
            parameters += f"{key}={val},"
        parameters = parameters.rstrip(",")
        request = f"APIKEY={self.apikey};EVENT=GET;TABLE={table};PARAMETERS=({parameters})"
        resp = self.send_request(request)
        return resp

    def update(self, table, data):
        request = f"APIKEY={self.apikey};EVENT=UPDATE;TABLE={table};DATA=[{data}]"
        resp = self.send_request(request)
        return resp

    def delete(self, table, delete_id):
        request = f"APIKEY={self.apikey};EVENT=DELETE;TABLE={table};PARAMETERS=(ID={delete_id})"
        resp = self.send_request(request)
        return resp

    def send_request(self, request):
        connection = self.connect_to_server()
        try:
            connection.send(request.encode())
            return connection.recv(1024)
        except Exception as e:
            raise Exception from e

    def connect_to_server(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client_socket.connect((self.server_address, self.server_port))
            print(f"Connected to {self.server_address} on port {self.server_port}")
        except Exception as e:
            raise Exception(f"Failed to connect to {self.server_address} on port {self.server_port}: {e}")

        return client_socket
