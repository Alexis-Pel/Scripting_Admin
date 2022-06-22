import psutil


def show_disk_partitions():
    """
    show alls partitions to disk stockage
    :return: psutil.disk_partitions: [(device=str, mountpoint=str, fstype=str, opts=str, maxfile=int, maxpath=int)]
    """
    return psutil.disk_partitions()


def show_disk_usage(path: str):
    """
    show usage of a disks
    :return: psutil.disk_usage(path): [(total=int, used=int, free=int, percent=float)]
    """
    return psutil.disk_usage(path)


def show_disk_io_counters(perdisks: bool):
    """
    show io counters of a disk
    :return: psutil.disk_io_counters(perdisk=False)
    """
    return psutil.disk_io_counters(perdisk=perdisks)


def get_all_metrics(show_disk_usage_path: str, show_disk_io_counters_perdisks: bool):
    """
    get all metrics of disk
    :param show_disk_usage_path:
    :param show_disk_io_counters_perdisks:
    :return: {"disk_partitions": , "disk_usage": , "disk_io_counter": )}
    """

    return {"disk_partitions": show_disk_partitions(), "disk_usage": show_disk_usage(show_disk_usage_path),
            "disk_io_counter": show_disk_io_counters(show_disk_io_counters_perdisks)}

