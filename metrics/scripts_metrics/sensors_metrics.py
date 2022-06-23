import psutil

import metrics.config.config_system as sy


def get_sensors_temperatures(fahrenheit: bool = False):
    """
    get hardware temperatures
    :return: Return hardware temperatures.
    """
    # run for Linux, FreeBSD
    return psutil.sensors_temperatures(fahrenheit)


def get_sensors_fans():
    """
    get hardware fans speed
    :return: Return hardware fans speed.
    """
    # run for Linux
    return psutil.sensors_fans()


def get_sensors_battery():
    """
    get battery status information
    :return: Return battery status information as a named tuple
    """
    # run for Linux, Windows, FreeBSD
    return psutil.sensors_battery()._asdict()


def get_sensors_all():
    """
    get all metrics
    :return: dictionary: all metrics
    """
    sensors_temperatures = None
    sensors_fans = None
    os = sy.get_my_os()

    if os == "FreeBSD":
        sensors_temperatures = get_sensors_temperatures()

    if os == "Linux":
        sensors_fans = get_sensors_fans()
        sensors_temperatures = get_sensors_temperatures()

    return {"sensors_battery": get_sensors_battery(), "sensor_temperature": sensors_temperatures,
            "sensor_fan": sensors_fans}


if __name__ == "__main__":
    print(get_sensors_all())
