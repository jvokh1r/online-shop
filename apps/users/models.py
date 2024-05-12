from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from .managers import CustomUserManager
from .validators import validate_phone_number


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
#
#     objects = UserManager()
#
#     EMAIL_FIELD = "email"
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []
#
#     def clean(self):
#         super().clean()
#         self.email = self.__class__.objects.normalize_email(self.email)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)

    objects = CustomUserManager()

    phone_number = models.CharField(max_length=17, validators=[validate_phone_number])
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=6, unique=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.get_full_name()

    class Meta:
        ordering = ['-pk']


class UserAuthCode(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=4)
    expire_at = models.DateTimeField(null=True)

