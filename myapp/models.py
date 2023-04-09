import datetime

from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.models import User



# Create your models here.
class slider(models.Model):
    DISCOUNT_DEAL = (
        ('HOT DEALS','HOT DEALS'),
        ('New Arraivels', 'New Arraivels'),

    )
    Image = models.ImageField(upload_to='media/slider_imgs')
    Discount_Deal = models.CharField(choices=DISCOUNT_DEAL,max_length=100)
    Sale = models.IntegerField()
    Brand_Name = models.CharField(max_length=200)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=200)

    def __str__(self):
        return self.Brand_Name



class banner_area(models.Model):
    image = models.ImageField(upload_to='media/banner_img')
    Discount_Deal = models.CharField(max_length=100)
    Quote = models.CharField(max_length=100)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.Quote





class Main_Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name



class Category(models.Model):
    main_category = models.ForeignKey(Main_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + "--" + self.main_category.name




class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.category.main_category.name + "--" + self.category.name + "--" + self.name



class Section(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Color(models.Model):
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.code


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Product(models.Model):
    total_quantity = models.IntegerField()
    availability = models.IntegerField()
    featured_image = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()
    tax = models.IntegerField(null=True)
    packing_cost = models.IntegerField(null=True)
    product_information = RichTextField()
    model_name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    categories = models.ForeignKey(Category,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE,null=True)
    tags = models.CharField(max_length=100)
    description = RichTextField()
    section = models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)

    def __str__(self):
         return self.product_name


    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_detail", kwargs={'slug': self.slug})

    class Meta:
        db_table = "myapp_Product"

def create_slug(instance, new_slug=None):
    slug = slugify(instance.product_name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Product)


class Coupon_Code(models.Model):
    code = models.CharField(max_length=100)
    discount = models.IntegerField()

    def __str__(self):
       return self.code




class Product_Image(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image_u = models.ImageField(upload_to='pro_img',default='')



class Additional_Ingformation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    amount = models.IntegerField(null=True,default='')
    payment_id = models.CharField(max_length=300,null=True,blank=True)
    paid = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.user.username



class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    product = models.CharField(max_length=200)
    image = models.ImageField(upload_to="media/Order_img")
    quantity = models.CharField(max_length=20)
    price = models.CharField(max_length=50)
    total = models.IntegerField()

    def __str__(self):
        return self.order.user.username


