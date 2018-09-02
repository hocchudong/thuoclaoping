import requests_mock

from django.contrib.auth.models import User
from django.test import TestCase, Client
from check.models import Group, Group_attribute, Host_attribute, Service, Host, Alert
from lib.utils import Auth


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.users = [User.objects.create(username='test', password='test'),
                      User.objects.create(username='test1', password='test1')]
        self.alert = Alert.objects.create(user=self.users[0],
                                          email_alert='nguyenvanminhkma@gmail.com',
                                          telegram_id='481523352',
                                          webhook='https://hooks.slack.com/services/'
                                                  'T43EZN8L8/BAH1W0F2M/'
                                                  'X6j7twjNgLWyu9PKodrD2OQs')
        self.services = [Service.objects.create(service_name='http'),
                         Service.objects.create(service_name='ping')]
        self.groups = [Group.objects.create(user=self.users[0],
                                            service=self.services[0],
                                            group_name='test_http_01',
                                            ok=10,
                                            warning=40, critical=90),
                       Group.objects.create(user=self.users[0],
                                            service=self.services[1],
                                            group_name='test_ping_01',
                                            ok=20,
                                            warning=50,
                                            critical=80)]
        self.group_attr = [Group_attribute.objects.create(group=self.groups[1],
                                                          attribute_name='interval_ping',
                                                          value=10,
                                                          type_value=0),
                           Group_attribute.objects.create(group=self.groups[1],
                                                          attribute_name='number_packet',
                                                          value=10,
                                                          type_value=0)]
        self.hosts = [Host.objects.create(hostname='host_test_1',
                                          group=self.groups[1]),
                      Host.objects.create(hostname='host_test_2',
                                          group=self.groups[1])]
        self.host_attr = [Host_attribute.objects.create(attribute_name='ip_address',
                                                        value='8.8.8.8',
                                                        type_value=4,
                                                        host=self.hosts[0]),
                          Host_attribute.objects.create(attribute_name='ip_address',
                                                        value='1.1.1.1',
                                                        type_value=4,
                                                        host=self.hosts[1])]

    def test_user(self):
        self.assertEqual(User.objects.get(username="test"), self.users[0])
        self.assertEqual(User.objects.get(username="test1"), self.users[1])

    def test_alert(self):
        user = User.objects.get(username="test")
        self.assertEqual(Alert.objects.get(user_id=user.id), self.alert)

    def test_services(self):
        self.assertEqual(Service.objects.get(service_name='http'), self.services[0])
        self.assertEqual(Service.objects.get(service_name='ping'), self.services[1])

    def test_group(self):
        self.assertEqual(Group.objects.get(group_name='test_http_01'), self.groups[0])
        self.assertEqual(Group.objects.get(group_name='test_ping_01'), self.groups[1])

    def test_group_attr(self):
        self.assertEqual(Group_attribute.objects.get(attribute_name='interval_ping'),
                         self.group_attr[0])
        self.assertEqual(Group_attribute.objects.get(attribute_name='number_packet'),
                         self.group_attr[1])

    def test_host(self):
        self.assertEqual(Host.objects.get(hostname='host_test_1'),
                         self.hosts[0])
        self.assertEqual(Host.objects.get(hostname='host_test_2'),
                         self.hosts[1])

    def test_host_attr(self):
        self.assertEqual(Host_attribute.objects.get(host=self.hosts[0]),
                         self.host_attr[0])
        self.assertEqual(Host_attribute.objects.get(host=self.hosts[1]),
                         self.host_attr[1])

    def test_login(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)

    def test_host_ping(self):
        response = self.client.get("/host/ping")
        self.assertEqual(response.status_code, 301)

    def test_host_http(self):
        response = self.client.get("/host/http")
        self.assertEqual(response.status_code, 301)


class TestInfluxDBClient(TestCase, Auth):
    """Set up the TestInfluxDBClient object."""

    def setUp(self):
        """Initialize an instance of TestInfluxDBClient object."""
        # By default, raise exceptions on warnings
        self.authen = Auth()
        self.cli = self.authen.auth(host_db='localhost',
                                    port=8086,
                                    username='username',
                                    password='password',
                                    database='database')
        self.dummy_points = [
            {
                "measurement": "cpu_load_short",
                "tags": {
                    "host": "server01",
                    "region": "us-west"
                },
                "time": "2009-11-10T23:00:00.123456Z",
                "fields": {
                    "value": 0.64
                }
            }
        ]

    def test_scheme(self):
        self.assertEqual('http://localhost:8086', self.cli._baseurl)

    def test_write(self):
        """Test write in TestInfluxDBClient object."""
        with requests_mock.Mocker() as m:
            m.register_uri(
                requests_mock.POST,
                "http://localhost:8086/write",
                status_code=204
            )
            # cli = InfluxDBClient(database='db')
            self.cli.write(
                {"database": "mydb",
                 "retentionPolicy": "mypolicy",
                 "points": [{"measurement": "cpu_load_short",
                             "tags": {"host": "server01",
                                      "region": "us-west"},
                             "time": "2009-11-10T23:00:00Z",
                             "fields": {"value": 0.64}}]}
            )

            self.assertEqual(
                m.last_request.body,
                b"cpu_load_short,host=server01,region=us-west "
                b"value=0.64 1257894000000000000\n",
            )
