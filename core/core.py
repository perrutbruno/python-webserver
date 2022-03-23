import socket
import threading


class Core:
    sock_addr = ('', 3010)

    lis_sock = (socket.AF_INET, socket.SOCK_STREAM)

    def initialize_socket_and_server():
        with socket.socket(Core.lis_sock[0], Core.lis_sock[1]) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(Core.sock_addr)
            print(f'LISTENING ON PORT {Core.sock_addr[1]}')
            s.listen(1)

            while True:
                try:
                    threading.Thread(name="")

                    conn, addr = s.accept()
                    print('to no try')
                    req_data = conn.recv(1024)

                    print(req_data.decode('utf-8'))
                    http_response = b"""\
HTTP/1.1 200 OK

Imagine that we have a default webserver page here :p ...!
"""
                    conn.sendall(http_response)
                    conn.close()

                except Exception:
                    conn.close()
                    s.accept()
                finally:
                    conn.close()
                    s.accept()


core = Core

core.initialize_socket_and_server()
