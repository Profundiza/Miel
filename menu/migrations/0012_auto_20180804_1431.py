# Generated by Django 2.0.5 on 2018-08-04 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_auto_20180804_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='unit_cost',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='receta',
            name='costo',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='receta',
            name='unit_cost',
            field=models.FloatField(null=True),
        ),
    ]
