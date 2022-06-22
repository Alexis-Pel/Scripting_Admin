import psutil


def get_boot_time():
    """
    Return the system boot time expressed in seconds since the epoch
    :return:
    """
    return psutil.boot_time()


def get_users():
    """
    Return users currently connected on the system as a list of named tuples including different fields
    :return:
    """
    return psutil.users()


def get_all_others_metrics():
    """
    Return all others metrics
    :return:
    """
    return{"boot_time": get_boot_time(), "users": get_users()}
