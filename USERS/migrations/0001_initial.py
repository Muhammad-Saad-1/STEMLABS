# Generated by Django 2.2.6 on 2019-11-24 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('f_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(max_length=15)),
                ('cnic', models.IntegerField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=1)),
                ('age', models.IntegerField(max_length=3)),
                ('image', models.ImageField(default='images/default_profile_kylie.jpg', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='USERS.Users')),
                ('is_admin', models.BooleanField(default=True)),
            ],
            bases=('USERS.users',),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='USERS.Users')),
                ('blood_group', models.CharField(max_length=3)),
                ('height', models.IntegerField(max_length=5)),
                ('weight', models.IntegerField(max_length=5)),
                ('is_patient', models.BooleanField(default=True)),
            ],
            bases=('USERS.users',),
        ),
        migrations.CreateModel(
            name='Physician',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='USERS.Users')),
                ('date_joined', models.DateField()),
                ('is_physician', models.BooleanField(default=True)),
                ('experience', models.IntegerField(max_length=2)),
            ],
            bases=('USERS.users',),
        ),
    ]
