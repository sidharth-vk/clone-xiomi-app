from django.db import models
from products.models import product
# Create your models here.

class Cart(models.Model):

    cart_id = models.CharField( max_length=250, blank=True)
    date_added = models.DateField( auto_now_add=True)
    razor_pay_order_id = models.CharField( max_length=100, null=True, blank=True)
    razor_pay_payment_id = models.CharField( max_length=100, null=True, blank=True)
    razor_pay_payment_signature = models.CharField( max_length=100, null=True, blank=True)


    class Meta:
        db_table= 'Cart'
        ordering= ['date_added']

    def __str__(self):
        return '{}'.format( self.cart_id)
    
class CartItem(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    
    class Meta:
        db_table='CartItem'
        
    def sub_total(self):
        return self.product.product_price * self.quantity
    
    def __str__(self):
        return '{}'.format( self.product )
    
        
        

