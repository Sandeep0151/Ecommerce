# Generated by Django 4.1.7 on 2023-03-27 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_order_orderitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(default=1),
        ),
    ]
