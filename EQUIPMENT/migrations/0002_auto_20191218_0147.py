# Generated by Django 2.2.5 on 2019-12-17 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EQUIPMENT', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='description',
            field=models.TextField(default='None'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
