import psutil
from metrics.config import config_system as sy
# Not Apple M1 : print(psutil.cpu_freq(percpu=False))


def get_cpu_times(per_cpu: bool = False):
    """
    Every attribute represents the seconds the CPU has spent
    :param per_cpu: function per cpu or not
    :return: system CPU times as a named tuple.
    """
    # --- run for alls --- #
    return psutil.cpu_times(percpu=per_cpu)._asdict()


def get_cpu_percent(per_cpu: bool = False, interval: int = 1):
    """
    get cpu percentage
    :param per_cpu: function per cpu or not
    :param interval: time before result
    :return: system cpu percent utilisation
    """
    # --- run for alls --- #
    return psutil.cpu_percent(percpu=per_cpu, interval=interval)


def get_cpu_times_percent(per_cpu: bool = False, interval: int = 1):
    """
    get cpu percentage
    :param per_cpu: function per cpu or not
    :param interval: time before result
    :return: system cpu time percent utilisation
    """
    # --- run for alls --- #
    return psutil.cpu_times_percent(percpu=per_cpu, interval=interval)._asdict()


def get_cpu_count(logical: bool = False):
    """
    get number of cpu's
    :param logical: all cores or just physical
    :return: get cpu counts
    """
    # --- run for alls --- #
    return psutil.cpu_count(logical=logical)


def get_cpu_stats():
    """
    get cpu different stats
    :return: cpu stats
    """
    # --- run for alls --- #
    return psutil.cpu_stats()._asdict()


def get_cpu_load_avg():
    """
    get cpu avg load utilisation
    :return: system cpu load avg
    """
    # --- run for alls --- #
    return psutil.getloadavg()[0]


def get_cpu_freq():
    """
    get frequence cpu
    :param
    :return: psutil.cpu_freq()
    """
    # --- run for linux only --- #
    return psutil.cpu_freq()


def get_cpu_all():
    """
    get all metrics
    :return: dictionary: all metrics
    """
    freq = None
    if sy.get_my_os() == "Linux":
        freq = get_cpu_freq()

    return {"cpu_time": get_cpu_times(), "percent": get_cpu_percent(),
            "time_percent": get_cpu_times_percent(), "count": get_cpu_count(),
            "stats": get_cpu_stats(), "load_avg": get_cpu_load_avg(), "freq": freq}
