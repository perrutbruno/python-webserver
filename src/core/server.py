from math import sin
import os
import socket
import json

from src.classes.oscheck import OSCheck
from http import HTTPStatus


class WServerCore:
    sock_addr = ('', 3010)

    lis_sock = (socket.AF_INET, socket.SOCK_STREAM)

    def search_for_page(page_name: str):
        oper_sys = OSCheck.check_os()

        oper_sys_path = OSCheck.build_path(oper_sys)

        for root, dir, files in os.walk(oper_sys_path):
            for file in files:
                if page_name == file:
                    status = HTTPStatus(200)
                    # return print(status, status.phrase)
                    f = open(f'{oper_sys_path}/{page_name}', 'r')
                    raw_file_data = f.readlines()

                    single_str_data = " ".join(raw_file_data)
                    return str(single_str_data)
                else:
                    status = HTTPStatus(404)
                    return print(status, status.phrase)

    def initialize_socket_and_server():
        with socket.socket(WServerCore.lis_sock[0], WServerCore.lis_sock[1]) as soc:
            soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            soc.bind(WServerCore.sock_addr)
            print(f'LISTENING ON PORT {WServerCore.sock_addr[1]}')
            soc.listen(1)

            while True:
                try:

                    conn, addr = soc.accept()
                    req_data = conn.recv(1024)

                    # print(req_data.decode('utf-8'))
                    http_response_header = b"""\
HTTP/1.1 200 OK

"""

                    # http_response_body = bytes("done", "utf8")

                    get_decoded_file_str = WServerCore.search_for_page(
                        'page.html')

                    http_response_body = bytes(get_decoded_file_str, "utf8")
                    message = http_response_header + http_response_body
                    # # print(http_response)
                    # print(http_response_header)
                    # print(http_response_body)
                    conn.sendall(message)
                    conn.close()

                except Exception:
                    conn.close()
                    soc.accept()

                finally:
                    conn.close()
                    soc.accept()
