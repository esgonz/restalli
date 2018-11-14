# Generated by Django 2.0.5 on 2018-11-14 01:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaMenu',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nombreCategoria', models.CharField(max_length=95)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ofertas',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
                ('fechaInicio', models.DateTimeField()),
                ('fechaTermino', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductosMenu',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nombreProducto', models.CharField(max_length=45)),
                ('slugProducto', models.SlugField(max_length=255, unique=True)),
                ('descripcion', models.CharField(max_length=250)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField()),
                ('restaurant_uuid', models.CharField(max_length=36)),
                ('user_uuid', models.CharField(max_length=36)),
                ('categoria_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.CategoriaMenu')),
            ],
        ),
        migrations.CreateModel(
            name='ProductosMenuStock',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('porciones', models.IntegerField()),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('productoStock_uuid', models.ManyToManyField(to='stock.ProductoStock')),
            ],
        ),
        migrations.AddField(
            model_name='productosmenu',
            name='productoStock_uuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.ProductosMenuStock'),
        ),
        migrations.AddField(
            model_name='ofertas',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.ProductosMenu'),
        ),
    ]
