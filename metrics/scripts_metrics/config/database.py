import logging
import os
import socket

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS


class database:
    TOKEN = os.environ.get("INFLUXDB_TOKEN")
    ORG = "scripting_admin_groupe5"
    URL = "https://europe-west1-1.gcp.cloud2.influxdata.com"
    BUCKET = "monitoring"

    client = InfluxDBClient(url=URL, token=TOKEN, org=ORG)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    query_api = client.query_api()
    point = None

    def set_point(self, point_name: str, field_name: str, value: float, tag_name: str = None, tag_value: str = None):
        if tag_name and tag_value:
            self.point = (
                Point(point_name)
                .tag(tag_name, tag_value)
                .tag("system", socket.gethostname())
                .field(field_name, float(value))
            )
        else:
            self.point = (
                Point(point_name)
                .tag("system", socket.gethostname())
                .field(field_name, float(value))
            )

    def send_metric(self):
        self.write_api.write(bucket=self.BUCKET, org=self.ORG, record=self.point)
        logging.info(f"data sent : {self.point}")
