import psutil


def get_sensors_temperatures(fahrenheit: bool = False):
    """
    get hardware temperatures
    :return: Return hardware temperatures.
    """

    return psutil.sensors_temperatures(fahrenheit)


def get_sensors_fans():
    """
    get hardware fans speed
    :return: Return hardware fans speed.
    """

    return psutil.sensors_fans()

def get_sensors_battery():
    """
    get battery status information
    :return: Return battery status information as a named tuple
    """

    return psutil.sensors_battery()

def get_sensors_all():
    """
    get all metrics
    :return: dictionary: all metrics
    """
    return {"sensors_temperatures": get_sensors_temperatures(),
            "sensors_fans": get_sensors_fans(),
            "sensors_battery": get_sensors_battery()}
