# Generated by Django 2.0.5 on 2018-11-13 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20181113_1948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoriamenu',
            old_name='_created',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='categoriamenu',
            old_name='_deleted',
            new_name='deleted',
        ),
        migrations.RenameField(
            model_name='categoriamenu',
            old_name='_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='categoriamenu',
            old_name='_updated',
            new_name='updated',
        ),
    ]
