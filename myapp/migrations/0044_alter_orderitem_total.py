# Generated by Django 4.1.7 on 2023-03-30 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0043_alter_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='total',
            field=models.IntegerField(),
        ),
    ]
