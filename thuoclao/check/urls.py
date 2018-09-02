from django.conf.urls import url, include
from check import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet, base_name='groups')
router.register(r'groupattributes', views.GroupAttributeViewSet, base_name='groupattributes')
router.register(r'hosts', views.HostViewSet, base_name='hosts')
router.register(r'hostattributes', views.HostAttributeViewSet, base_name='hostattributes')


urlpatterns = [
    url(r'^.*\.html', views.view_html, name='view_html'),

    # The home page
    url(r'^$', views.index, name='index'),

    # Support
    url(r'^help/$', views.help, name='help'),

    # The config host page
    url(r'^host/(?P<service_name>[-\w]+)/$', views.host, name='host'),
    url(r'^host/(?P<service_name>[-\w]+)/delete/(?P<host_id>\d+)/$', views.delete_host, name='delete_host'),
    url(r'^host/(?P<service_name>[-\w]+)/delete_group/(?P<group_id>\d+)/$', views.delete_group, name='delete_group'),
    url(r'^host/(?P<service_name>[-\w]+)/edit/(?P<host_id>\d+)/$', views.edit_host, name='edit_host'),
    url(r'^host/(?P<service_name>[-\w]+)/edit_group/(?P<group_id>\d+)/$', views.edit_group, name='edit_group'),
    url(r'^ajax/get_data/(?P<pk_host>\d+)/(?P<service_name>[-\w]+)/(?P<query_time>\d+)/$', views.get_data, name='get_data'),
    url(r'^ajax/total_parameter/$', views.total_parameter, name='total_parameter'),
    url(r'^ajax/info_influx/$', views.total_info_influxdb, name='total_info_influxdb'),
    url(r'^ajax/http_queries/$', views.get_http_queries, name='get_http_queries'),
    url(r'^ajax/server_errors/$', views.server_errors, name='server_errors'),
    url(r'^ajax/client_errors/$', views.client_errors, name='client_errors'),
    url(r'^ajax/cpu_util/$', views.cpu_util, name='cpu_util'),
    url(r'^ajax/ram/$', views.ram_info, name='ram_info'),
    url(r'^ajax/network/(?P<interface>[-\w]+)/$', views.network_info, name='network_info'),
    url(r'^ajax/disk/$', views.disk_info, name='disk_info'),
    url(r'^alert$', views.alert, name='alert'),
    url(r'^information$', views.information, name='information'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api/groups/$', views., name='groups'),
]
