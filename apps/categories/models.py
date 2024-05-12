from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to='categories/')
    product_counts = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sub Categories'
