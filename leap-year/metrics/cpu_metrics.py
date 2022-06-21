import psutil


# Not Apple M1 : print(psutil.cpu_freq(percpu=False))


def get_cpu_times(per_cpu: bool = False):
    """
    Every attribute represents the seconds the CPU has spent
    :param per_cpu: function per cpu or not
    :return: system CPU times as a named tuple.
    """
    return psutil.cpu_times(percpu=per_cpu)


def get_cpu_percent(per_cpu: bool = False, interval: int = 1):
    """
    get cpu percentage
    :param per_cpu: function per cpu or not
    :param interval: time before result
    :return: system cpu percent utilisation
    """
    return psutil.cpu_percent(percpu=per_cpu, interval=interval)


def get_cpu_times_percent(per_cpu: bool = False, interval: int = 1):
    """
    get cpu percentage
    :param per_cpu: function per cpu or not
    :param interval: time before result
    :return: system cpu time percent utilisation
    """
    return psutil.cpu_times_percent(percpu=per_cpu, interval=interval)


def get_cpu_count(logical: bool = False):
    """
    get number of cpu's
    :param logical: all cores or just physical
    :return: get cpu counts
    """
    return psutil.cpu_count(logical=logical)


def get_cpu_stats():
    """
    get cpu different stats
    :return: cpu stats
    """
    return psutil.cpu_stats()


def get_cpu_load_avg():
    """
    get cpu avg load utilisation
    :return: system cpu load avg
    """
    return psutil.getloadavg()


def get_cpu_all():
    """
    get all metrics
    :return: dictionary: all metrics
    """
    return {"cpu_time": get_cpu_times(), "cpu_percent": get_cpu_percent(),
            "cpu_time_percent": get_cpu_times_percent(), "cpu_count": get_cpu_count(),
            "cpu_stats": get_cpu_stats(), "cpu_load_avg": get_cpu_load_avg()}
