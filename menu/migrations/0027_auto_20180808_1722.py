# Generated by Django 2.0.5 on 2018-08-08 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0026_auto_20180808_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetacomp',
            name='medida',
            field=models.CharField(choices=[('oz', 'oz'), ('lb', 'lb'), ('gal', 'gal'), ('L', 'L'), ('mL', 'mL'), ('g', 'g'), ('kg', 'kg'), ('unit', 'unit'), ('dozen', 'dozen')], default='testma', max_length=30),
        ),
    ]
