# Generated by Django 2.0.6 on 2018-07-17 09:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20180716_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 17, 9, 25, 29, 452090, tzinfo=utc)),
        ),
    ]