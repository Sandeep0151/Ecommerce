# Generated by Django 4.1.7 on 2023-03-27 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_alter_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
