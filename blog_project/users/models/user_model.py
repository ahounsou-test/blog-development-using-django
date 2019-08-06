from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager

from xlib.django.models import CountryField
from xlib.enums import Gender

class UserManager(AbstractUserManager):
    pass


class User(AbstractUser):

    phone = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    birthday = models.DateField(null=True)
    gender = models.CharField(choices=Gender.values(), max_length=6)
    country = CountryField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    objects = UserManager()


    def __repr__(self):
        return f"id: {self.id} username: {self.username}"

    class Meta:
        db_table = 'user'
