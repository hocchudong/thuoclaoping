from rest_framework import serializers
from .models import Group, Group_attribute, Host, Host_attribute


class GroupSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Group
        fields = '__all__'


class GroupAttributeSerializer(serializers.ModelSerializer):
    # group = GroupSerializer()

    def get_group(self):
        group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.filter(user=self.request.user))
        return group

    class Meta:
        model = Group_attribute
        fields = '__all__'


class HostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Host
        fields = '__all__'


class HostAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host_attribute
        fields = '__all__'
