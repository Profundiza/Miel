# Generated by Django 2.0.5 on 2018-08-04 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20180803_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='code',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]