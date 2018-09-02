from influxdb import InfluxDBClient


def auth(host_db=None, port=None, username=None,
         password=None, database=None):
    host_db = host_db or '192.168.100.57'
    port = port or 8086
    username = username or 'minhkma'
    password = password or 'minhkma'
    database = database or 'thuoclao'
    client = InfluxDBClient(host=host_db, port=port, username=username,
                            password=password, database=database)
    return client


def threshold_ping(hosts, interval_time, measurements, oke, warning, critical):
    client = auth()
    for host in hosts:
        data = client.query('select mean(loss) from {} '
                            'where host=\'{}\' and time > (now() - {}m)'
                            .format(measurements, host, interval_time))
        results = list(data.get_points(measurement='moisture'))
        # for result in results:
        #     value = result['mean']
        #     value_time = result['time']
    return results
