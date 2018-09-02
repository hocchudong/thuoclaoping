import smtplib
import requests
import json

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from urllib import request
from django.db import models


class Alert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email_alert = models.EmailField(max_length=100, blank=True)
    telegram_id = models.CharField(max_length=10, help_text="Telegram ID", blank=True)
    webhook = models.URLField(help_text="URL to send message into Slack.", blank=True)
    delay_check = models.IntegerField(help_text="Interval time to check status host. - unit: second", default=10)

    def __str__(self):
        return str(self.user)

    def send_email(self, from_add, cc_add_list, subject,
                   message, password, smtpserver):
        to_addr_list = []
        to_addr_list.append(self.email_alert)
        mes = 'From: {}\nTo: {}\nCc: {}\nSubject: {}\n{}'\
            .format(from_add, ','.join(to_addr_list),
                    ','.join(cc_add_list),
                    subject, message)

        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(from_add, password)
        server.sendmail(from_add, to_addr_list, mes)
        server.quit()

    def send_telegram_message(self, token, text):
        url = 'https://api.telegram.org/bot{0}/sendMessage'.format(token)
        data = {'chat_id': self.telegram_id, 'text': text, 'parse_mode': 'Markdown'}
        requests.post(url=url, data=data).json()

    def send_slack_message(self, text):
        payload = {"text": "{0}".format(text)}
        try:
            json_data = json.dumps(payload)
            req = request.Request(self.webhook, data=json_data.encode('ascii'),
                                  headers={'Content-Type': 'application/json'})
            request.urlopen(req)
        except Exception as em:
            print("EXCEPTION: " + str(em))

    class Meta:
        ordering = ('user',)


class Service(models.Model):
    service_name = models.CharField(max_length=45)

    def __str__(self):
        return str(self.service_name)

    class Meta:
        ordering = ('service_name',)


class Group(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    group_name = models.CharField(max_length=45)
    description = models.TextField(null=True, blank=True)
    ok = models.IntegerField(help_text="", null=True, blank=True)
    warning = models.IntegerField(help_text="", null=True, blank=True)
    critical = models.IntegerField(help_text="", null=True, blank=True)

    def __str__(self):
        return str(self.group_name)


class Group_attribute(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    attribute_name = models.CharField(max_length=45)
    value = models.CharField(max_length=100)
    type_value = models.IntegerField(null=True, help_text="0: integer, 1: bool, 2: date, 3: string, 4: ip-domain, 5: URL")

    def __str__(self):
        return str(self.attribute_name) + " - " + str(self.value)


class Host(models.Model):
    hostname = models.CharField(max_length=45)
    description = models.TextField(null=True, blank=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    status = models.IntegerField(help_text="0: ok, 1: warning, 2: critical", default=-1)

    def __str__(self):
        return str(self.hostname)

    class Meta:
        ordering = ('hostname',)


class Host_attribute(models.Model):
    host = models.ForeignKey('Host', on_delete=models.CASCADE)
    attribute_name = models.CharField(max_length=45)
    value = models.CharField(max_length=100)
    type_value = models.IntegerField(null=True, help_text="0: integer, 1: bool, 2: date, 3: string, 4: ip-domain, 5: URL")

    def __str__(self):
        return str(self.attribute_name) + " - " + str(self.value)


# UserProfile model will be automatically created/updated when we create/update User instances.
@receiver(post_save, sender=User)
def create_group_profile(sender, instance, created, **kwargs):
    if created:
        ping = Service.objects.get(service_name="ping")
        http = Service.objects.get(service_name="http")
        group_ping = Group.objects.create(user=instance, service=ping, group_name="Ping Default",
                                          description="", ok=10, warning=40, critical=100)
        group_http = Group.objects.create(user=instance, service=http, group_name="HTTP Default",
                                          description="")

        Group_attribute.objects.create(group=group_ping, attribute_name='interval_ping',
                                       value=20, type_value=0)

        Group_attribute.objects.create(group=group_ping, attribute_name='number_packet',
                                       value=20, type_value=0)

        Group_attribute.objects.create(group=group_http, attribute_name='interval_check',
                                       value=20, type_value=0)
