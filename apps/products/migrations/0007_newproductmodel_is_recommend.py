# Generated by Django 4.1.5 on 2023-06-07 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_allmedia_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='newproductmodel',
            name='is_recommend',
            field=models.BooleanField(default=False, null=True, verbose_name='is_recommend'),
        ),
    ]
