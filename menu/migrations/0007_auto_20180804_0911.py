# Generated by Django 2.0.5 on 2018-08-04 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_remove_platillo_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
