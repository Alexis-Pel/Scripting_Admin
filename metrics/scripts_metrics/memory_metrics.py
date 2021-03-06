import psutil


def get_virtual_memory():
    """
    get virtual memory
    :return: return statistics about system memory usage as a named tuple
    """
    # run for All

    return psutil.virtual_memory()._asdict()


def get_swap_memory():
    """
    get swap memory
    :return: Return system swap memory statistics as a named tuple
    """
    # run for All

    return psutil.swap_memory()._asdict()


def get_memory_all():
    """
    get all metrics
    :return: dictionary: all metrics
    """
    return {"memory_all": get_virtual_memory(), "swap_memory": get_swap_memory()}
