import platform
import logging
logging.basicConfig(level=logging.INFO)


def get_my_os():
    os = platform.system()
    logging.info(f"Operating System: {os}")
    return os