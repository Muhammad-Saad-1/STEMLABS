# Generated by Django 2.2.5 on 2019-12-14 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERS', '0009_auto_20191214_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(max_length=1),
        ),
    ]
