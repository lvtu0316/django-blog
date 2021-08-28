# Generated by Django 2.2.3 on 2021-08-28 10:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20210828_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 28, 10, 17, 9, 742754, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.IntegerField(choices=[(0, '通过'), (1, '不通过')], default=0, verbose_name='审核状态'),
        ),
    ]
