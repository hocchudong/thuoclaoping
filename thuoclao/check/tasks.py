import re
import asyncio

from datetime import datetime
from influxdb import InfluxDBClient
from requests_futures.sessions import FuturesSession
from celery.utils.log import get_task_logger
from celery import shared_task
from django.contrib.auth.models import User

from .models import Alert, Host, Service, Group
from lib.display_metric import Display
from thuoclao import settings


logger = get_task_logger(__name__)


def get_fping():
    users = User.objects.all()
    data = {}
    for user in users:
        service = Service.objects.get(service_name='ping')
        user = User.objects.get(username=user.username)
        all_groups = Group.objects.filter(user_id=user.id, service=service)
        all_hosts = Host.objects.filter(group__in=all_groups)
        hosts = []
        for host in all_hosts:
            item = {'id': host.id, 'hostname': host.hostname, 'status': host.status,
                    'description': host.description, 'group_name': host.group.group_name}
            ip_addr = host.host_attribute_set.get(attribute_name='ip_address')
            item['ip_address'] = ip_addr.value
            item['number_packet'] = host.group.group_attribute_set.get(attribute_name='number_packet').value
            item['interval_ping'] = host.group.group_attribute_set.get(attribute_name='interval_ping').value
            hosts.append(item)
        data[user.username] = hosts
    return data


def get_http():
    users = User.objects.all()
    data = {}
    for user in users:
        service = Service.objects.get(service_name='http')
        user = User.objects.get(username=user.username)
        all_groups = Group.objects.filter(user_id=user.id, service=service)
        all_hosts = Host.objects.filter(group__in=all_groups)
        hosts = []
        for host in all_hosts:
            item = {'id': host.id, 'hostname': host.hostname, 'status': host.status,
                    'description': host.description, 'group_name': host.group.group_name}
            item['interval_check'] = host.group.group_attribute_set.get(attribute_name='interval_check').value
            url = host.host_attribute_set.get(attribute_name='url')
            item['url'] = url.value
            hosts.append(item)
        data[user.username] = hosts
    return data


fping_regex = re.compile(
    r"(?P<host>[^ ]+)\s*:.+=\s*(?P<sent>\d+)/(?P<recv>\d+)/(?P<loss>\d+)"
    r"(.+=\s*(?P<min>[0-9.]+)/(?P<avg>[0-9.]+)/(?P<max>[0-9.]+))?")


def write_influxdb(data, user, hostname, group_name,
                   host_db=None, port=None, username=None,
                   password=None, database=None):
    host_db = host_db or settings.INFLUXDB_HOST
    port = port or settings.INFLUXDB_PORT
    username = username or settings.INFLUXDB_USER
    password = password or settings.INFLUXDB_USER_PASSWORD
    database = database or settings.INFLUXDB_DB
    client = InfluxDBClient(host=host_db, port=port, username=username,
                            password=password, database=database)
    json_body = [
        {
            "measurement": "ping",
            "tags": {
                "username": str(user),
                "ip": str(data.group("host")),
                "group": str(group_name),
                "hostname": str(hostname)
            },
            "fields": {
                "sent": int(data.group("sent")) if data.group("sent") else 0,
                "recv": int(data.group("recv")) if data.group("recv") else 0,
                "loss": int(data.group("loss")) if data.group("loss") else 0,
                "min": float(data.group("min")) if data.group("min") else 0.0,
                "avg": float(data.group("avg")) if data.group("avg") else 0.0,
                "max": float(data.group("max")) if data.group("max") else 0.0
            }
        }
    ]
    client.write_points(json_body)


async def custom_sleep(interval, user, hostname, group_name, stdout, stderr):
    await asyncio.sleep(interval)
    print(type(interval))
    print(stdout, stderr)
    for line in stderr.decode().split('\n'):
        data = fping_regex.match(line)
        if data:
            write_influxdb(data=data, user=user, hostname=hostname,
                           group_name=group_name)
    print('SLEEP {}\n'.format(datetime.now()))


async def factorial(interval, user, hostname, group, *args):
    process = await asyncio.create_subprocess_shell(
        *args,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    await custom_sleep(interval, user, hostname, group, stdout, stderr)


async def loop_exec(loop, interval, user,
                    hostname, group_name, number_packet, ip):
    while loop.is_running():
        tasks = [
            asyncio.ensure_future(factorial(interval,
                                            user,
                                            hostname,
                                            group_name,
                                            'fping -c {0} {1}'
                                            .format(number_packet, ip)))
        ]
        await asyncio.wait(tasks)
    loop.call_soon(loop.create_task, loop_exec(loop, interval, user,
                                               hostname, group_name,
                                               number_packet, ip))


session = FuturesSession()


def bg_cb(sess, resp, hostname, group_name, user, host_db=None, port=None,
          username=None, password=None, database=None):
    host_db = host_db or settings.INFLUXDB_HOST
    port = port or settings.INFLUXDB_PORT
    username = username or settings.INFLUXDB_USER
    password = password or settings.INFLUXDB_USER_PASSWORD
    database = database or settings.INFLUXDB_DB
    client = InfluxDBClient(host=host_db, port=port, username=username,
                            password=password, database=database)
    json_body = [
        {
            "measurement": "http",
            "tags": {
                "url": str(resp.url),
                'hostname': str(hostname),
                'group': str(group_name),
                'username': str(user)
            },
            "fields": {
                "code": int(resp.status_code),
                "response": float(resp.elapsed.total_seconds())
            }
        }
    ]
    client.write_points(json_body)


async def http_exec(loop, url, interval, hostname, group_name, user):
    future = session.get(url, background_callback=lambda sess,
                         resp: bg_cb(sess, resp, hostname=hostname,
                                     group_name=group_name, user=user))

    loop.call_later(int(interval), loop.create_task,
                    http_exec(loop, url, int(interval),
                    hostname, group_name, user))


async def http():
    logger.info("run def http")
    data_http = get_http()
    print(data_http)
    loop = asyncio.get_event_loop()
    for user in data_http:
        for count, info_url in enumerate(data_http[user]):
            url = info_url['url']
            hostname = info_url['hostname']
            group_name = info_url['group_name']
            interval = int(info_url['interval_check'])

            loop.call_soon(loop.create_task, http_exec(loop, url, interval,
                                                       hostname, group_name, user))
    loop.run_forever()


async def fping():
    logger.info("run def ping")
    loop = asyncio.get_event_loop()
    data_ping = get_fping()
    print(data_ping)
    for user in data_ping:
        for count, info_ping in enumerate(data_ping[user]):
            ip = info_ping['ip_address']
            hostname = info_ping['hostname']
            group_name = info_ping['group_name']
            interval = int(info_ping['interval_ping'])
            number_packet = info_ping['number_packet']

            loop.call_soon(loop.create_task, loop_exec(loop, interval, user,
                           hostname, group_name, number_packet, ip))
    loop.run_forever()


def handle_notification(user_id):
    user = User.objects.get(id=user_id)
    alert = Alert.objects.get(user=user)
    groups = Group.objects.filter(user=user)
    hosts = Host.objects.filter(group__in=groups)

    for host in hosts:
        print(user.username + " - " + host.hostname)
        display = Display(host.group.group_name, host.hostname, host.group.user.username)
        if host.group.service.service_name == "ping":
            alert_data = display.check_ping_notify(host.group.ok, host.group.warning, host.group.critical)

            if alert_data[0] != host.status:  # status changed
                host.status = alert_data[0]
                host.save()
                ip_address = host.host_attribute_set.get(attribute_name='ip_address').value
                email_title = "[{}] Notify to check {}".format(alert_data[3], host.hostname)
                email_message = "Hostname {} \nAddress {} \nLoss {}% - {}".format(host.hostname, ip_address,
                                                                                  alert_data[1], alert_data[3])
                tele_slack_message = """
                *[{0}] Notify to check !!! {1}*
                ```
                Host : {1}
                Adress : {2}
                Loss : {3}%
                Status : {0}
                ```
                """.format(alert_data[3], host.hostname, ip_address, alert_data[1])
                sending(alert, email_title, email_message, tele_slack_message)

        elif host.group.service.service_name == "http":
            alert_data = display.check_http_notify()

            if alert_data[0] != host.status:  # status changed
                host.status = alert_data[0]
                host.save()
                url = host.host_attribute_set.get(attribute_name='url').value
                email_title = "[{}] Notify to check {}".format(alert_data[3], host.hostname)
                email_message = "Hostname {} \nURL {} \nHTTP Code {} - {}".format(host.hostname, url,
                                                                                  alert_data[1], alert_data[3])
                tele_slack_message = """
                *[{0}] Notify to check !!! {1}*
                ```
                Host : {1}
                URL : {2}
                HTTP Code : {3}
                Status : {0}
                ```
                """.format(alert_data[3], host.hostname, url, alert_data[1])
                sending(alert, email_title, email_message, tele_slack_message)


def sending(alert, email_title, email_message, tele_slack_message):
    if alert.email_alert:
        alert.send_email(settings.FROM_EMAIL, [], email_title,
                         email_message, settings.PASSWD_MAIL, settings.SMTP_SERVER)

    if alert.telegram_id:
        alert.send_telegram_message(settings.TOKEN, tele_slack_message)

    if alert.webhook:
        alert.send_slack_message(tele_slack_message)


async def notify():
    all_user = User.objects.all()
    loop = asyncio.get_event_loop()
    for user in all_user:
        try:
            alert = Alert.objects.get(user=user)
            interval = alert.delay_check
            loop.call_soon(loop.create_task, notice_to_each_user(loop, user, interval))
        except Alert.DoesNotExist:
            continue
    loop.run_forever()


async def notice_to_each_user(loop, user, interval):
    print("Notice user : " + user.username)
    handle_notification(user.id)
    loop.call_later(interval, loop.create_task, notice_to_each_user(loop, user, interval))


@shared_task
def run():
    task1 = asyncio.ensure_future(fping())
    task2 = asyncio.ensure_future(http())
    task3 = asyncio.ensure_future(notify())
    loop = asyncio.get_event_loop()
    loop.run_forever()


run()
