
from django.db import models

class product(models.Model):
    
    CATEGORY = (
        ('MOBILE','MOBILE'),
        ('ELECTRONICS','ELECTRONICS'),
    )
    
    product_name = models.CharField(max_length=50)
    product_discription = models.CharField(max_length=150)
    product_price_original = models.IntegerField()
    product_price = models.IntegerField( )
    product_category = models.CharField( max_length=50, choices= CATEGORY )
    product_image = models.ImageField()
    stock = models.IntegerField()
    rating = models.IntegerField()
    def __str__(self):
        return self.product_name