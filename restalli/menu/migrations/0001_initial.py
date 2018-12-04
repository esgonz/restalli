# Generated by Django 2.0.5 on 2018-12-04 04:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
        ('comun', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaMenu',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=95)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comun.Estados')),
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
            ],
        ),
        migrations.CreateModel(
            name='ProductosMenu',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=45)),
                ('slug', models.SlugField(max_length=255)),
                ('descripcion', models.CharField(max_length=250)),
                ('imagen', models.ImageField(blank=True, default='nodisponible.png', upload_to='productos_menu')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('user_uuid', models.CharField(max_length=36)),
                ('categoria_uuid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.CategoriaMenu')),
                ('restaurant_uuid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comun.Restaurantes')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comun.Estados')),
            ],
        ),
        migrations.CreateModel(
            name='ProductosMenuStock',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('porciones', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('productoStock_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.ProductoStock')),
                ('productosMenu_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.ProductosMenu')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comun.Estados')),
            ],
        ),
        migrations.AddField(
            model_name='ofertas',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.ProductosMenu'),
        ),
        migrations.AddField(
            model_name='ofertas',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comun.Estados'),
        ),
    ]
