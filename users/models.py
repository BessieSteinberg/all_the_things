from django.db import models
from django.contrib.auth.models import User as DjangoUser


class User(DjangoUser):
    display_name = models.CharField(blank=True, max_length=255)
