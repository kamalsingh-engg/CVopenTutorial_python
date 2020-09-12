from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)
client.create_database("ddddffd")
print("database created ")