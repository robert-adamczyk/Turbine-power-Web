from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_company = models.BooleanField('Is Company', default=False)
    is_member = models.BooleanField('Is Member', default=True)

    def __str__(self):
        return f"{self.username} mail: {self.email}"
