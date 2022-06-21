import argparse
import logging

import tristan_bissextile

parser = argparse.ArgumentParser()
parser.add_argument('-year', help='année à tester', type=int)
args = parser.parse_args()

year = args.year
if tristan_bissextile.bissextile(year):
    logging.warning("L'année est une année bissextile!")
else:
    logging.warning("L'année n'est pas une année bissextile!")
