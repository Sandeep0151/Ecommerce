# Generated by Django 4.1.7 on 2023-03-26 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_alter_order_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='Product_img/Order_img')),
                ('quantity', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=50)),
                ('total', models.CharField(max_length=1000)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.order')),
            ],
        ),
    ]
