from django.db import models
from apps.features.models import ProductFeature
from django.core.validators import MinValueValidator


class Cart(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    product_feature = models.ForeignKey(ProductFeature, on_delete=models.PROTECT)
    counts = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return {self.product_feature.name}
