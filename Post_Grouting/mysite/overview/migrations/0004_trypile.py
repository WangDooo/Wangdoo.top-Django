# Generated by Django 2.0.6 on 2018-07-24 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0003_originalpile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trypile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
