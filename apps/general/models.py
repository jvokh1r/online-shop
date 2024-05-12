from django.db import models
from django.core.exceptions import ValidationError
from django_ckeditor_5.fields import CKEditor5Field
from .validators import validate_phone_number


class General(models.Model):
    store_name = models.CharField(max_length=20)
    delivery_price = models.FloatField(default=0)
    logo = models.ImageField(upload_to='logos/%Y/%m/%d')
    phone_number = models.CharField(max_length=17, validators=[validate_phone_number])
    email = models.EmailField()
    address = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    desc = CKEditor5Field('Text', config_name='extends')

    class Meta:
        verbose_name_plural = 'General'


class Service(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    icon = models.ImageField(upload_to='icons/services/')

    def __str__(self):
        return self.title


class Branch(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)
    icon = models.ImageField(upload_to='branches/')


class Banner(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    desc = CKEditor5Field('Text', config_name='extends')

    def __str__(self):
        return self.title


class Coupon(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text='Enter in UZS or in percent')
    amount_is_percent = models.BooleanField(default=False)

    def clean(self):
        if self.amount_is_percent and not (1 <= self.amount <= 100):
            raise ValidationError({'amount': 'Invalid amount [1, 100]'})

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    icon = models.ImageField(upload_to='icons/socials/')
    link = models.URLField()

    def __str__(self):
        return self.name


class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

