from django.db import models
from apps.users.models import CustomUser


class Contact(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    title = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return {self.name} - {self.message}
