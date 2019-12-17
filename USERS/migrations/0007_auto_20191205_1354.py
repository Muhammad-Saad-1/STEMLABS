# Generated by Django 2.2.6 on 2019-12-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERS', '0006_auto_20191128_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('primary_key', models.IntegerField()),
                ('user_type', models.CharField(choices=[('patient', 'patient'), ('admin', 'admin'), ('physician', 'physician')], max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='password',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_name',
        ),
        migrations.AlterField(
            model_name='patient',
            name='height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='weight',
            field=models.IntegerField(),
        ),
    ]
