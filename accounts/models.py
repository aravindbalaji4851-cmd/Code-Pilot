from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):   #AbstractUser contains username password password_encryption .. (inherited)

    phone = models.CharField(max_length=12,unique=True)

    ROLE_CHOICES = (
        ("student","student"),
        ("admin","admin")
    )

    role = models.CharField(max_length=200,choices=ROLE_CHOICES,default="student")
