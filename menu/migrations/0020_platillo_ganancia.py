# Generated by Django 2.0.5 on 2018-08-05 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0019_auto_20180805_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='platillo',
            name='ganancia',
            field=models.FloatField(null=True),
        ),
    ]