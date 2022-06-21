import psutil


# Not Apple M1 : print(psutil.cpu_freq(percpu=False))


def get_cpu_times():
    return psutil.cpu_times()


def get_cpu_percent(per_cpu: bool = False, interval: int = 1):
    return psutil.cpu_percent(percpu=per_cpu, interval=interval)


def get_cpu_times_percent(per_cpu: bool = False, interval: int = 1):
    return psutil.cpu_times_percent(percpu=per_cpu, interval=interval)


def get_cpu_count(logical: bool = False):
    return psutil.cpu_count(logical=logical)


def get_cpu_stats():
    return psutil.cpu_stats()


def get_cpu_load_avg():
    return psutil.getloadavg()


def get_cpu_all():
    return {"cpu_time": get_cpu_times(), "cpu_percent": get_cpu_percent(),
            "cpu_time_percent": get_cpu_times_percent(), "cpu_count": get_cpu_count(),
            "cpu_stats": get_cpu_stats(), "cpu_load_avg": get_cpu_load_avg()}
