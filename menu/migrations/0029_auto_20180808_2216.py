# Generated by Django 2.0.5 on 2018-08-09 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0028_auto_20180808_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='restaurante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='menu.Restaurante'),
        ),
    ]