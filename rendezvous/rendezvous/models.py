from django.db import models

class Availabilities(models.Model):
    user = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE,
    )
    av_time = models.DateTimeField()

class Users(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    phone = models.CharField(max_length=10)
    fullname = models.CharField(max_length=30)
