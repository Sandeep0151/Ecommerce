# Generated by Django 4.1.7 on 2023-03-30 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0044_alter_orderitem_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_image',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product_image',
            name='image_u',
            field=models.ImageField(default='', upload_to='media/pro_img'),
        ),
    ]