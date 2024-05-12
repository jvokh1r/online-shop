from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import MinValueValidator


class Product(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    old_price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    short_desc = models.CharField(max_length=100)
    long_desc = CKEditor5Field('Text', config_name='extends')
    review_counts = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
