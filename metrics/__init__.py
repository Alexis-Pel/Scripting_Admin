import argparse
import logging
import os
import sys
import time
from metrics.config import database

from metrics.scripts_metrics import sensors_metrics as sensors, memory_metrics as memory, cpu_metrics as cpu, \
    disk_metrics as disk, network_metrics as network, others_metrics as others

logging.basicConfig(level=logging.INFO, filename=f"{os.getcwd()}/metrics/metrics.log", filemode='w',
                    format='%(message)s')
parser = argparse.ArgumentParser()
parser.add_argument('-i',
                    dest='seconds',
                    help='in seconds for the interval of the logs',
                    type=str
                    )

args = parser.parse_args()
db = database.database()


def get_all_metrics(interval: int):
    """
    Get All the metrics from the components
    :return: dictionary: all_metrics
    """
    all_metrics = {'cpu': cpu.get_cpu_all(), 'memory': memory.get_memory_all(), 'disk': disk.get_all_metrics(),
                   'network': network.get_all_network_metrics(), 'sensors': sensors.get_sensors_all(),
                   'others': others.get_all_others_metrics()}
    
    send_metrics(all_metrics)
    time.sleep(interval)
    get_all_metrics(interval)


def send_metrics(metrics):
    for component in metrics:
        for key in metrics[component]:
            try:
                if type(metrics[component][key]) == dict:
                    for tag in metrics[component][key]:
                        if type(metrics[component][key][tag]) == int or type(metrics[component][key][tag]) == float:
                            db.set_point(field_name=key, value=metrics[component][key][tag], point_name=component,
                                         tag_name="details", tag_value=tag)
                            db.send_metric()
                else:
                    db.set_point(field_name=key, value=metrics[component][key], point_name=component)
                    db.send_metric()
            except TypeError as e:
                logging.error(e)


if __name__ == "__main__":
    try:
        seconds = int(args.seconds) if args.seconds.isdigit() else logging.error("Please use digit") and sys.exit(0)
    except AttributeError:
        logging.critical(" Please use argument -i [seconds]")
        sys.exit(0)

    get_all_metrics(seconds)
