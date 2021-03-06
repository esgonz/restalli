# Generated by Django 2.0.5 on 2018-12-04 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productostock',
            name='categoria',
            field=models.CharField(choices=[('FRU', 'Frutas'), ('VER', 'Verduras y hortalizas'), ('OTR', 'Otros'), ('DES', 'Despensa'), ('FLA', 'Frescos y Lacteos'), ('PAS', 'Pastaleria'), ('BEB', 'Bebidas y Licores'), ('PPD', 'Productos Preparados'), ('CNG', 'Congelados'), ('PES', 'Pescados y Mariscos'), ('CAR', 'Carnes rojas y blancas'), ('PAN', 'Panaderia')], default='OTR', max_length=3),
        ),
    ]
