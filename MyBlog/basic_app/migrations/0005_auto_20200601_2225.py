# Generated by Django 2.0.13 on 2020-06-01 16:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_auto_20200405_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 1, 16, 55, 46, 758527, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 1, 16, 55, 46, 758527, tzinfo=utc)),
        ),
    ]
