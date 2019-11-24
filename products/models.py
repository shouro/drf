from django.db import models


class ProductAttribute(models.Model):
    property = models.CharField(max_length=40)
    value = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.property}_{self.value}'

class ProductPrice(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    begin_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{str(self.price)}_{self.begin_date}_{self.end_date}'

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    attributes = models.ManyToManyField(ProductAttribute)
    prices = models.ManyToManyField(ProductPrice)

    class Meta:
        ordering = ('-created_at',)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.name
