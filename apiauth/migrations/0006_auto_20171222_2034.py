# Generated by Django 2.0 on 2017-12-22 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apiauth', '0005_auto_20171222_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfriendship',
            name='friendship',
        ),
        migrations.RemoveField(
            model_name='userfriendship',
            name='user',
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='user',
        ),
        migrations.AddField(
            model_name='friendship',
            name='action_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friendship',
            name='status',
            field=models.IntegerField(choices=[(0, 'PENDING'), (1, 'ACCEPTED'), (2, 'DECLINED'), (3, 'BLOCKED')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friendship',
            name='user1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friendship',
            name='user2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='UserFriendship',
        ),
    ]
