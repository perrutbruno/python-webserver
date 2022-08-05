from concurrent.futures import thread
from threading import Thread

import os
import socket

from src.classes.oscheck import OSCheck
from http import HTTPStatus


class WServerCore:
    def __init__(self, port_num=3010):
        self.sock_addr = ('', 3010)

        self.lis_sock = (socket.AF_INET, socket.SOCK_STREAM)

    def search_for_page(self, page_name: str):
        oper_sys = OSCheck.check_os()
        files_list = []

        oper_sys_path = OSCheck.build_path(oper_sys)

        for root, dir, files in os.walk(oper_sys_path):
            for file in files:
                files_list.append(file)
                if page_name == file:
                    status = HTTPStatus(200)
                    f = open(f'{oper_sys_path}/{page_name}', 'r')
                    raw_file_data = f.readlines()

                    single_str_data = " ".join(raw_file_data)
                    return str(single_str_data)

        if page_name not in files:
            status = HTTPStatus(404)
            f = open(f'{oper_sys_path}/notfound.html', 'r')
            raw_file_data = f.readlines()

            single_str_data = " ".join(raw_file_data)
            return str(single_str_data)

    def initialize_socket_and_server(self):
        with socket.socket(self.lis_sock[0], self.lis_sock[1]) as soc:
            soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            soc.bind(self.sock_addr)
            print(f'LISTENING ON PORT {self.sock_addr[1]}')
            soc.listen(1)
            while True:
                thread = Thread(target=self.handle_connection, args=(soc,))
                thread.start()

    def handle_connection(self, soc):
        try:
            conn, addr = soc.accept()
            req_data = conn.recv(2048)
            decoded_req = req_data.decode('utf-8')
            http_response_header = b"""\
HTTP/1.1 200 OK

"""

            cut_decoded_req = decoded_req[4:19].split()
            list_cut_decoded_req = cut_decoded_req[0].split()
            url_path = list_cut_decoded_req[0]
            url_path = url_path.split()[0]
            url_path = url_path[1:]

            if "/favicon.ico" in url_path:
                return

            if ".html" not in url_path:
                url_path = url_path + ".html"

            get_decoded_file_str = self.search_for_page(
                url_path)

            http_response_body = bytes(get_decoded_file_str, "utf8")
            message = http_response_header + http_response_body
            conn.sendall(message)
            conn.close()

        except Exception:
            conn.close()
            soc.accept()

        finally:
            conn.close()
            soc.accept()
