# Generated by Django 4.1.5 on 2023-05-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_alter_checkout_charge_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='comment'),
        ),
    ]