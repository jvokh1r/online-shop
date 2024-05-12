from django.db import models
from django.core.validators import MinValueValidator
from apps.features.models import ProductFeature
from apps.users.models import CustomUser
from apps.general.models import PaymentMethod
from .validators import validate_phone_number


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    payment_method_name = models.CharField(max_length=50, blank=True)

    total_price = models.FloatField(default=0)
    coupon_price = models.FloatField(default=0)
    delivery_price = models.FloatField(default=0)
    is_paid = models.BooleanField(default=False)

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=30, blank=True, validators=[validate_phone_number])
    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=6, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {self.first_name} - {self.last_name}


class OrderProduct(models.Model):
    product_feature = models.ForeignKey(ProductFeature, on_delete=models.PROTECT)
    counts = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_feature.name
