# Generated by Django 2.0.5 on 2018-12-02 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0003_auto_20181202_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='tipoPago',
            field=models.CharField(choices=[('EFE', 'EFECTIVO'), ('CHE', 'CHEQUE'), ('CRE', 'CREDITO'), ('DEB', 'DEBITO')], default='EFE', max_length=3),
        ),
    ]
