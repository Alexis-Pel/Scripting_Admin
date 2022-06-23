import platform
import logging
import socket


def get_my_os():
    os = platform.system()
    logging.debug(f"Operating System: {os}")
    return os


def get_my_hostname():
    return socket.gethostname()
