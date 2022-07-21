from ast import arg
import multiprocessing
from time import sleep
from src.core.server import WServerCore
from src.classes import oscheck
import threading
core = WServerCore

# core.initialize_socket_and_server()
if __name__ == '__main__':
    loop = True
    _results = []
    while loop:
        # t = threading.Thread(name='webpage handler',
        #                      target=core.search_for_page, args=["page.html", ])
        t = threading.Thread(name="webserver",
                             target=core.initialize_socket_and_server, args=[])
        t.start()

        loop = False

    #p = Process(target=core.search_for_page, args=(queue, 'teste3.html'))

    # multiprocessing.freeze_support()
    # with multiprocessing.Pool() as pool:
    #print(pool.map(core.search_for_page, "teste.html"))

    # print(retorno)
