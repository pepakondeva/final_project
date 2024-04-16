from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from final_project.account.manager import AppUserManager
from final_project.core.validators import max_size_of_the_photo


class BookipediaUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    objects = AppUserManager()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
    )
    last_name = models.CharField(
        max_length=25,
    )

    age = models.PositiveIntegerField()

    profile_image = models.ImageField(
        upload_to='profile_picture/',
        validators=(max_size_of_the_photo,),
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        BookipediaUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

