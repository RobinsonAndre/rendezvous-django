# Generated by Django 3.0.3 on 2020-02-09 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rendezvous', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availabilities',
            old_name='username',
            new_name='user',
        ),
    ]
