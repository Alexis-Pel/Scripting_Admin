import psutil


def get_net_io_counters(per_nic : bool = False, no_wrap : bool = True):
    """
    Return system-wide network I/O statistics as a named tuple including differents attributes
    :param per_nic:
    :param no_wrap:
    :return: tuple including different attributes
    """
    return psutil.net_io_counters(pernic=per_nic, nowrap=no_wrap)


def get_net_connections(kind: str = "inet"):
    """
    Return system-wide socket connections as a list of named tuples
    :param kind:
    :return:
    """
    return psutil.net_connections(kind=kind)


def get_net_if_addrs():
    """
    Return the addresses associated to each NIC installed on the system
    :return: list of named tuples
    """
    return psutil.net_if_addrs()


def get_net_if_stats():
    """
    Return information about each NIC installed on the system
    :return: 
    """
    return psutil.net_if_stats()


def get_all_network_metrics():
    """
    get all metrics of network
    :return: dictionnary : all metrics
    """
    return {"io_counters": get_net_io_counters(), "connections": get_net_connections(),
            "if_stats": get_net_if_stats(), "if addrs": get_net_if_addrs()}
