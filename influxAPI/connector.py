from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision, Dialect
from influxdb_client.client.write_api import SYNCHRONOUS


def connectToInfluxDB(datas):
    token = "Rc9O02UKh6AY144KcP4VbVryr8Er2dBuyGfy0o1B70lPezcx2MlpAuUs7R3uy8yqznRrt5PbgpBSAyV0LWskTA=="
    org = "Emot"
    bucket = "test"

    client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)

    write_api = client.write_api(write_options=SYNCHRONOUS)

    p = Point("my_measurement").tag("location", "Banglore").field("data", datas)
    write_api.write(bucket=bucket, org=org, record=p)

    query_api = client.query_api()
    tables = query_api.query(org=org, query='from(bucket:"test")\
    |> range(start: -10m)\
    |> filter(fn:(r) => r._measurement == "my_measurement")\
    |> filter(fn: (r) => r.location == "Banglore")\
    |> filter(fn:(r) => r._field == "data" )')

    results = []
    for item in tables:
        for record in item.records:
            results.append((record.get_field(), record.get_value()))

    print(results)
