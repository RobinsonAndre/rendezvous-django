from rest_framework import serializers


from rendezvous.models import Users, Availabilities


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields='phone', 'fullname'

class AvailabilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Availabilities
        fields='user','av_time'
