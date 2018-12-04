# Generated by Django 2.0.5 on 2018-12-04 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='tipoPago',
            field=models.CharField(choices=[('DEB', 'DEBITO'), ('CHE', 'CHEQUE'), ('EFE', 'EFECTIVO'), ('CRE', 'CREDITO')], default='EFE', max_length=3),
        ),
    ]
