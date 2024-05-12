from django.db import models
from apps.users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator


class Comment(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    message = models.CharField(max_length=300)
    name = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
