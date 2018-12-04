# Generated by Django 2.0.5 on 2018-12-04 04:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comun', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('usuario', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=8)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1)),
                ('personas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comun.Personas')),
            ],
        ),
    ]
