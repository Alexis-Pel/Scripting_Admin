import os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import socket


class database:
    TOKEN = os.environ.get("INFLUXDB_TOKEN")
    ORG = "scripting_admin_groupe5"
    URL = "https://europe-west1-1.gcp.cloud2.influxdata.com"
    BUCKET = f"metrics_{socket.gethostname()}"

    client = InfluxDBClient(url=URL, token=TOKEN, org=ORG)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    query_api = client.query_api()
    point = None

    def set_point(self, point_name: str, field_name: str, value: float):
        self.point = (
            Point(point_name)
            .field(field_name, float(value))
        )

    def send_metric(self):
        self.write_api.write(bucket=self.BUCKET, org=self.ORG, record=self.point)
