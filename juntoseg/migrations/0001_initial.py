# Generated by Django 3.1.6 on 2021-02-10 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_column='useEmail', default='', max_length=255, unique=True, verbose_name='email address')),
                ('name', models.CharField(db_column='useName', default='', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='useDateJoined')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='useDateUpdate')),
                ('is_admin', models.BooleanField(db_column='useIsAdmin', default=False)),
                ('is_active', models.BooleanField(db_column='useIsActive', default=False)),
            ],
            options={
                'db_table': 'User',
                'managed': True,
            },
        ),
    ]
