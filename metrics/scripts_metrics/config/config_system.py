import platform
import logging
import socket
logging.basicConfig(level=logging.INFO)


def get_my_os():
    os = platform.system()
    logging.info(f"Operating System: {os}")
    return os


def get_my_hostname():
    return socket.gethostname()
