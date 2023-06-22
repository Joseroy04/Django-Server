from django.conf import settings
from django.db import models

class CustomUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("User"), on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, null=True)
    email = models.EmailField(("Email id"), max_length=254,null=True)
    # Add any other custom fields or methods as needed
