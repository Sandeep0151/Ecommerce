# Generated by Django 4.1.7 on 2023-03-30 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0045_remove_product_image_image_url_product_image_image_u'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_image',
            name='image_u',
            field=models.ImageField(default='', upload_to='pro_img'),
        ),
    ]
