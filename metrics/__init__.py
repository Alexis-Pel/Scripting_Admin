import argparse
import logging
import sys
from typing import Any

import cpu_metrics as cpu

logging.basicConfig(level=logging.INFO)
parser = argparse.ArgumentParser()
parser.add_argument('-i',
                    dest='seconds',
                    help='in seconds for the interval of the logs',
                    type=str
                    )

args = parser.parse_args()


def get_all_metrics(interval: int):
    """
    Get All the metrics from the components
    :return: dictionary: all_metrics
    """
    all_metrics = {}

    cpu_metrics: {str: Any} = cpu.get_cpu_all()
    all_metrics['cpu_metrics'] = cpu_metrics
    print(all_metrics, interval)


if __name__ == "__main__":
    try:
        seconds = int(args.seconds) if args.seconds.isdigit() else logging.error("Please use digit") and sys.exit(0)
    except AttributeError:
        logging.critical(" Please use argument -i [seconds]")
        sys.exit(0)
    get_all_metrics(seconds)
