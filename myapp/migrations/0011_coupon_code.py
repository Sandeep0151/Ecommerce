# Generated by Django 4.1.7 on 2023-03-25 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_product_packing_cost_product_tax'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon_Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('dicount', models.IntegerField()),
            ],
        ),
    ]
