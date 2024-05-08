from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.utils.html import mark_safe

class Banner(models.Model):
    img = models.ImageField(upload_to="banner_imgs/")
    alt_text = models.CharField(max_length = 300)

    class Meta:
        verbose_name_plural = '1. Banners'

    def image_tag_path(self):
        return mark_safe('<img src="%s" width="100"/>' %(self.img.url))

    def __str__(self):
        return self.alt_text


class Category(models.Model):
    title=models.CharField(max_length=180)
    image=models.ImageField(upload_to="cat_imgs/", null=True)

    class Meta:
        verbose_name_plural = '2. Categories'

    def image_tag_path(self):
        return mark_safe('<img src="%s" width="50" height="30" />' %(self.image.url))

    def __str__(self):
        return self.title


class Marca(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="marca_imgs/", null=True)

    class Meta:
        verbose_name_plural = '3. Marcas'

    def __str__(self):
        return self.title


class Color(models.Model):
    title=models.CharField(max_length=100)
    color_codigo=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '4. Colors'

    def color_tag_path(self):
        return mark_safe('<div style="width:50px; height:30px; background:%s"></div>' % (self.color_codigo))

    def __str__(self):
        return self.title
    

class Size(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '5. Sizes'

    def __str__(self):
        return self.title
    

class Product(models.Model):
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=400)
    detail=models.TextField()
    specs=models.TextField()
    marca=models.ForeignKey(Marca, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    color=models.ForeignKey(Color, on_delete=models.CASCADE)
    size=models.ForeignKey(Size, on_delete=models.CASCADE)
    status=models.BooleanField(default=True)
    produto_em_destaque=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '6. Products'

    def __str__(self):
        return self.title
    

class ProductAttribute(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    image=models.ImageField(upload_to="product_imgs/", null=True)

    class Meta:
        verbose_name_plural = '7. ProductAttributes'

    def __str__(self):
        return self.product.title
    
    def image_tag_path(self):
        return mark_safe('<img src="%s" width="50" height="30" />' %(self.image.url))