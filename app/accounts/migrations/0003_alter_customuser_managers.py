# Generated by Django 4.2.9 on 2024-02-25 09:58

import accounts.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', accounts.managers.CustomUserManager()),
            ],
        ),
    ]
