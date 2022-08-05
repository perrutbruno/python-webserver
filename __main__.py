from src.core.server import WServerCore
from src.classes import oscheck

import multiprocessing
from time import sleep

import threading

core = WServerCore()

# core.initialize_socket_and_server()
if __name__ == '__main__':
    loop = True
    while loop:
        core.initialize_socket_and_server()
        loop = False
