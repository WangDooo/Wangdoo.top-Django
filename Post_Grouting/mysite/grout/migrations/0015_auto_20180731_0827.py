# Generated by Django 2.0.6 on 2018-07-31 00:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('grout', '0014_surplus_remaining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
