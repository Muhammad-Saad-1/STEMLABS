# Generated by Django 2.2.6 on 2019-11-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERS', '0002_auto_20191124_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='cnic',
            field=models.BigIntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.BigIntegerField(max_length=15),
        ),
    ]
