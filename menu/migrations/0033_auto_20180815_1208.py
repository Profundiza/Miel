# Generated by Django 2.0.5 on 2018-08-15 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0032_auto_20180810_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platilloing',
            name='medida',
            field=models.CharField(choices=[('oz', 'oz'), ('lb', 'lb'), ('gal', 'gal'), ('L', 'L'), ('mL', 'mL'), ('g', 'g'), ('kg', 'kg'), ('unit', 'pieza'), ('dozen', 'docena')], max_length=30),
        ),
        migrations.AlterField(
            model_name='platilloing',
            name='platillo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.Platillo'),
        ),
        migrations.AlterField(
            model_name='platillorec',
            name='medida',
            field=models.CharField(choices=[('oz', 'oz'), ('lb', 'lb'), ('gal', 'gal'), ('L', 'L'), ('mL', 'mL'), ('g', 'g'), ('kg', 'kg'), ('unit', 'pieza'), ('dozen', 'docena')], max_length=30),
        ),
        migrations.AlterField(
            model_name='platillorec',
            name='receta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.Receta'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='medida',
            field=models.CharField(choices=[('oz', 'oz'), ('lb', 'lb'), ('gal', 'gal'), ('L', 'L'), ('mL', 'mL'), ('g', 'g'), ('kg', 'kg'), ('unit', 'pieza'), ('dozen', 'docena')], max_length=30),
        ),
        migrations.AlterField(
            model_name='recetacomp',
            name='medida',
            field=models.CharField(choices=[('oz', 'oz'), ('lb', 'lb'), ('gal', 'gal'), ('L', 'L'), ('mL', 'mL'), ('g', 'g'), ('kg', 'kg'), ('unit', 'pieza'), ('dozen', 'docena')], max_length=30),
        ),
        migrations.AlterField(
            model_name='recetacomp',
            name='receta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.Receta'),
        ),
    ]
