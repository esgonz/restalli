# Generated by Django 2.0.5 on 2018-12-04 04:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('estado', models.CharField(max_length=95)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidoPaterno', models.CharField(max_length=50)),
                ('apellidoMaterno', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=1)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurantes',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('razonSocial', models.CharField(max_length=150)),
                ('rut', models.CharField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=250)),
                ('comuna', models.CharField(max_length=120)),
                ('ciudad', models.CharField(max_length=120)),
                ('telefono', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('restaurante_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comun.Restaurantes')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comun.Estados')),
            ],
        ),
        migrations.AddField(
            model_name='personas',
            name='restaurante_uuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comun.Restaurantes'),
        ),
    ]
