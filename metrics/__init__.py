import argparse
import logging
import os
import sys
import time

import psutil

import database

import cpu_metrics as cpu

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
    all_metrics = {'cpu': cpu.get_cpu_all()}

    logging.info(all_metrics)
    time.sleep(interval)
    send_metrics(all_metrics)
    time.sleep(interval)
    get_all_metrics(interval)


def send_metrics(metrics):
    for component in metrics:
        for key in metrics[component]:
            db.set_point(field_name=key, value=metrics[component][key], point_name=component)
            db.send_metric()


if __name__ == "__main__":
    try:
        seconds = int(args.seconds) if args.seconds.isdigit() else logging.error("Please use digit") and sys.exit(0)
    except AttributeError:
        logging.critical(" Please use argument -i [seconds]")
        sys.exit(0)

    get_all_metrics(seconds)
