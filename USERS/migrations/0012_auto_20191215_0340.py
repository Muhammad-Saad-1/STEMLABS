# Generated by Django 2.2.5 on 2019-12-14 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERS', '0011_auto_20191214_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(default='media/images/profile/default_profile_kylie.jpg', upload_to='media/images/profile'),
        ),
    ]
