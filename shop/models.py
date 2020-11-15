from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    parent = models.ForeignKey(Category, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'SubCategories'

    def __str__(self):
        return self.slug


class Shopproduct(models.Model):
    product_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255,default="uncategorise")
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_img = models.ImageField(upload_to="productimg")
    category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE)
    product_subcategory = models.ForeignKey(Subcategory,related_name='subproducts', on_delete=models.CASCADE)
    product_desc = models.TextField()
    product_pdate = models.DateField()
    product_stock = models.IntegerField()

    def __str__(self):
        return self.product_name

class Contactform(models.Model):
    person_name = models.CharField(max_length=50)
    person_email = models.EmailField()
    person_phone = models.BigIntegerField()
    person_msg = models.TextField()

    def __str__(self):
        return self.person_email