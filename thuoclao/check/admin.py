from django.contrib import admin

from .models import Alert, Host, Host_attribute, Service, Group, Group_attribute

admin.site.register(Alert)
admin.site.register(Host)
admin.site.register(Host_attribute)
admin.site.register(Service)
admin.site.register(Group)
admin.site.register(Group_attribute)
