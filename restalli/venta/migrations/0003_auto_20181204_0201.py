# Generated by Django 2.0.5 on 2018-12-04 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0002_auto_20181203_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='tipoPago',
            field=models.CharField(choices=[('CRE', 'CREDITO'), ('EFE', 'EFECTIVO'), ('CHE', 'CHEQUE'), ('DEB', 'DEBITO')], default='EFE', max_length=3),
        ),
    ]
