# Generated by Django 2.1.3 on 2018-11-14 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoriamenu',
            old_name='nombreCategoria',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='productosmenu',
            old_name='nombreProducto',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='productosmenu',
            old_name='slugProducto',
            new_name='slug',
        ),
        migrations.AlterField(
            model_name='categoriamenu',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comun.Estados'),
        ),
        migrations.AlterField(
            model_name='ofertas',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comun.Estados'),
        ),
        migrations.AlterField(
            model_name='productosmenu',
            name='categoria_uuid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.CategoriaMenu'),
        ),
        migrations.AlterField(
            model_name='productosmenu',
            name='restaurant_uuid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comun.Restaurantes'),
        ),
        migrations.AlterField(
            model_name='productosmenu',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comun.Estados'),
        ),
        migrations.AlterField(
            model_name='productosmenustock',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comun.Estados'),
        ),
    ]