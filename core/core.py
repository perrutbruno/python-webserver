import socket


class Core:
    addr = ("", 3010)

    listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    listening_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    listening_socket.bind(addr)

    listening_socket.listen(1)

    def initialize_socket():
        while True:
            print('LISTENING ON PORT ')
            client_connection, client_address = Core.listening_socket.accept()
            request_data = client_connection.recv(1024)
            print(request_data.decode('utf-8'))


core = Core

core.initialize_socket()
