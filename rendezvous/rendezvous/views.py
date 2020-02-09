from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime

from rendezvous.serializers import UsersSerializer, AvailabilitiesSerializer
from rendezvous.models import Users, Availabilities

STATUS_FAIL = {'status':'fail'}
STATUS_SUCCESS = {'status':'success'}

class UserView(APIView):
    def get(self,request):
        users = Users.objects.all()
        userializer = UsersSerializer(users, many=True)
        return Response(userializer.data)

class AvailView(APIView):
    def get(self,request):
        user = request.query_params.get('user')
        if user:
            avail = Availabilities.objects.filter(user=user)
        else:
            avail = Availabilities.objects.all()
        serial = AvailabilitiesSerializer(avail, many=True)
        return Response(serial.data)

class SameTimeView(APIView):
    def get(self,request):
        r_data = request.query_params
        if r_data.get('username'):
            user1 = r_data.get('username')
        else:
            return Response({'status':'fail'})
        # user1 = 'andre3'
        avail = Availabilities.objects.all()
        user_avail_times = set()
        for ava in avail:
            if (ava.user.username == user1):
                user_avail_times.add(ava.av_time)
        common_times = []
        for ava in avail:
            if (ava.av_time in user_avail_times and (ava.user.username != user1)):
                common_times.append(ava)
        serial = AvailabilitiesSerializer(common_times, many=True)
        return Response(serial.data)

class InsertAvail(APIView):
    def post(self,request):
        if not (
            'user' in request.data and
            'av_time' in request.data
        ):
            return Response(STATUS_FAIL)
        in_user = Users.objects.filter(username=request.data['user']).first()
        new_entry = Availabilities(
            user=in_user,
            av_time=datetime.strptime(request.data['av_time'], '%Y-%m-%d %H:%M:%S') )
        new_entry.save()
        return Response(STATUS_SUCCESS)

class InsertUser(APIView):
    def post(self,request):
        if not (
            'username' in request.data and
            'phone' in request.data and
            'fullname' in request.data
        ):
            return Response(STATUS_FAIL)
        new_entry = Users(
            username=request.data['username'],
            phone=request.data['phone'],
            fullname=request.data['fullname'])
        new_entry.save()
        return Response(STATUS_SUCCESS)
