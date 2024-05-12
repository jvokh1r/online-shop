from django.db import models
from apps.products.models import Product


class Wishlist(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name_plural = 'Wish List'
