# Generated by Django 4.1.7 on 2023-03-25 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_coupon_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon_code',
            old_name='dicount',
            new_name='discount',
        ),
    ]