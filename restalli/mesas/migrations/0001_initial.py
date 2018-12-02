# Generated by Django 2.0.5 on 2018-11-30 03:42

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
            name='Mesas',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('identificador', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=20)),
                ('pedido', models.CharField(max_length=10)),
                ('empleado', models.CharField(max_length=50)),
                ('fecha', models.CharField(max_length=50)),
                ('inicio', models.CharField(max_length=50)),
                ('termino', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1)),
                ('sucursal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comun.Sucursal')),
            ],
        ),
    ]