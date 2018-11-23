# Generated by Django 2.1.1 on 2018-11-21 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20181121_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriastock',
            name='nombreCategoria',
            field=models.CharField(choices=[('FRU', 'FRUTA'), ('VER', 'CARNE'), ('BEB', 'BEBIDAS_LICORES'), ('EFE', 'CONGELADOS'), ('DES', 'DESPENSAS'), ('FRE', 'FRESCOS_LACTEOS')], default='CAR', max_length=3),
        ),
        migrations.AlterField(
            model_name='stock',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comun.Estados'),
        ),
    ]