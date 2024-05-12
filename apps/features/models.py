from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from apps.products.models import Product


class Feature(models.Model):
    category = models.ForeignKey('categories.Category', on_delete=models.PROTECT, blank=True)
    sub_category = models.ForeignKey('categories.SubCategory', on_delete=models.PROTECT, blank=True)
    ordering_number = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def clean(self):
        if not self.category == self.sub_category.category:
            print(self.sub_category.category)
            raise ValidationError('You are supposed to choose right categories!')

    def __str__(self):
        return self.name


class FeatureValue(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='values')
    price = models.DecimalField(max_digits=20, decimal_places=1, default=0)
    value = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.feature}: {self.value}'

    class Meta:
        unique_together = ('feature', 'value')


class ProductFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # watch
    feature_value = models.ForeignKey(FeatureValue, on_delete=models.CASCADE) # black
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return str(self.feature_value)

    class Meta:
        unique_together = ('product', 'feature_value')
