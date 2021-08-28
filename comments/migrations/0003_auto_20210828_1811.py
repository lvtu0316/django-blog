# Generated by Django 2.2.3 on 2021-08-28 10:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20200414_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.IntegerField(default=0, verbose_name='审核状态'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 28, 10, 11, 51, 717564, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]