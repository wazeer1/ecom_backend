from django.db import models
from main.models import *
from colorfield.fields import ColorField

# Create your models here.
class Category(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=255,blank=True,null=True)
    class Meta:
        db_table = 'products_category'
        verbose_name ='category'
        verbose_name_plural ='catogories'

    def __str__(self):
        return self.category


class SubCategory(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sub_category = models.CharField(max_length=255,blank=True,null=True)
    category = models.ForeignKey('products.Category',on_delete=models.CASCADE,blank=True,null=True)
    class Meta:
        db_table = 'products_subcategory'
        verbose_name ='sub_category'
        verbose_name_plural ='sub_catogories'

    def __str__(self):
        return self.sub_category



class Product(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    price = models.PositiveIntegerField(default=0)
    offer = models.PositiveIntegerField(default=0)
    sub_category = models.ForeignKey('products.SubCategory',on_delete=models.CASCADE,blank=True,null=True)
    about_product = models.TextField(blank=True,null=True)
    model_name = models.CharField(max_length=255,blank=True,null=True)
    company = models.ForeignKey('products.company',on_delete=models.CASCADE,blank=True,null=True)
    class Meta:
        db_table = 'products_product'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name


class ProductImages(BaseModel):
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE)
    image = models.FileField(upload_to='media/product')
    is_cover = models.BooleanField(default=False)

    class Meta:
        db_table = 'products_product_image'
        verbose_name = 'product_image'
        verbose_name_plural = 'product_images'

    def __str__(self):
        return self.product.name
    
class AboutProduct(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    feature = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_about'
        verbose_name = 'product_about'
        verbose_name_plural = 'product_abouts'

    def __str__(self):
        return self.feature
    

class ProductColors(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    color = models.CharField(max_length=255,blank=True,null=True)
    color_code = ColorField(format="hexa")
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_color'
        verbose_name = 'product_color'
        verbose_name_plural = 'product_color'

    def __str__(self):
        return self.color
    
class Company(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,blank=True,null=True)
    logo = models.FileField(upload_to='media/compony')
    class Meta:
        db_table = 'products_company'
        verbose_name = 'product_company'
        verbose_name_plural = 'product_companies'

    def __str__(self):
        return self.name


class Banners(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.FileField(upload_to='media/banner')
    description = models.CharField(max_length=255,blank=True,null=True)
    product = models.ForeignKey('products.product',blank=True,null=True,on_delete=models.CASCADE)
    category = models.ForeignKey('products.Category',blank=True,null=True,on_delete=models.CASCADE)
    sub_category = models.ForeignKey('products.SubCategory',blank=True,null=True,on_delete=models.CASCADE)
    company = models.ForeignKey('products.company',blank=True,null=True,on_delete=models.CASCADE)
    class Meta:
        db_table = 'products_banner'
        verbose_name = 'banner'
        verbose_name_plural = 'banners'

    def __str__(self):
        return self.product.name
