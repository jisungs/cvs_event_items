from django.db import models

# Create your models here.
class Product(models.Model):
    product_name  = models.CharField(max_length=250)
    price         = models.CharField(max_length=250, blank=True)
    images        = models.ImageField(upload_to='photos/products')
    img_url       = models.CharField(max_length=250, blank=True)
    event_type    = models.CharField(max_length=250, blank=True)
    created_data  = models.DateTimeField(auto_created=True , null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)
    market        = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.product_name