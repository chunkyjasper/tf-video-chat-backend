# Generated by Django 2.0 on 2017-12-22 21:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apiauth', '0006_auto_20171222_2034'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together={('user1', 'user2')},
        ),
    ]
