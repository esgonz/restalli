# Generated by Django 2.1.1 on 2018-11-26 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfiles',
            old_name='usuario',
            new_name='user',
        ),
    ]
