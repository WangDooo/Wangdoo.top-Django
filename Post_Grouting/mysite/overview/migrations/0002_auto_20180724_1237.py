# Generated by Django 2.0.6 on 2018-07-24 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalpile',
            name='number',
            field=models.IntegerField(),
        ),
    ]
