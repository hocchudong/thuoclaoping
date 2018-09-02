import configparser

from influxdb import InfluxDBClient
from django.contrib.auth.models import User
from check.models import Host, Service
from thuoclao import settings


class GetConfig(object):
    def get_config(self, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        return config


class Auth(GetConfig):
    def auth(self, host_db=None, port=None, username=None, password=None, database=None):
        host_db = host_db or settings.INFLUXDB_HOST
        port = port or settings.INFLUXDB_PORT
        username = username or settings.INFLUXDB_USER
        password = password or settings.INFLUXDB_USER_PASSWORD
        database = database or settings.INFLUXDB_DB
        client = InfluxDBClient(host=host_db, port=port, username=username,
                                password=password, database=database)
        return client


class Sqlite(object):
    def get_sql(self):
        dict_users = {}
        users = User.objects.all()
        for user in users:
            dict_hosts = {}
            hosts = Host.objects.filter(user_id=user.id)
            services = Service.objects.filter(host__in=hosts).distinct()
            for ser in services:
                IPs = []
                for ser_info in ser.host.all():
                    IPs.append(ser_info.ip_address)
                dict_hosts[ser.service_name] = IPs
            dict_users[user.username] = dict_hosts
        return dict_users
