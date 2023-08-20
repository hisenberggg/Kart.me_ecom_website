from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('clothes','CLOTHES'),
    ('accessories', 'ACCESSORIES'),
    ('grooming','GROOMING'),
    ('electronics','ELECTRONICS')
)

STATUS_CHOICES = (
    ('received','RECEIVED'),
    ('accepted', 'ACCEPTED'),
    ('declined','DECLINED'),
    ('shipped','SHIPPED'),
    ('delivered','DELIVERED')
)

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    description = models.TextField(max_length=200)
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000)])
    product_image = models.ImageField(upload_to="products/")
    in_cart = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    date_of_purchase = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='received')
    def __str__(self) -> str:
        return self.product.name
