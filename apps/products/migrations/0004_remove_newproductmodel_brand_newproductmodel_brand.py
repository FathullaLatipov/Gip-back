# Generated by Django 4.1.5 on 2023-05-02 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_newproductmodel_color_newproductmodel_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newproductmodel',
            name='brand',
        ),
        migrations.AddField(
            model_name='newproductmodel',
            name='brand',
            field=models.ManyToManyField(blank=True, related_name='new_brand', to='products.brand', verbose_name='brand'),
        ),
    ]
