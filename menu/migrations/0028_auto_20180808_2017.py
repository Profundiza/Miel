# Generated by Django 2.0.5 on 2018-08-09 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0027_auto_20180808_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='platilloing',
            name='medida',
            field=models.CharField(choices=[('oz', 'oz'), ('lb', 'lb'), ('gal', 'gal'), ('L', 'L'), ('mL', 'mL'), ('g', 'g'), ('kg', 'kg'), ('unit', 'unit'), ('dozen', 'dozen')], default='temp', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platillorec',
            name='medida',
            field=models.CharField(choices=[('oz', 'oz'), ('lb', 'lb'), ('gal', 'gal'), ('L', 'L'), ('mL', 'mL'), ('g', 'g'), ('kg', 'kg'), ('unit', 'unit'), ('dozen', 'dozen')], default='temp', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recetacomp',
            name='medida',
            field=models.CharField(choices=[('oz', 'oz'), ('lb', 'lb'), ('gal', 'gal'), ('L', 'L'), ('mL', 'mL'), ('g', 'g'), ('kg', 'kg'), ('unit', 'unit'), ('dozen', 'dozen')], max_length=30),
        ),
    ]
