# Generated by Django 4.1.5 on 2023-05-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newproductmodel',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]