# Generated by Django 4.1.7 on 2023-03-26 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
