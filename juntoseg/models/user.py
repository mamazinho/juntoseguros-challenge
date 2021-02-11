from __future__ import unicode_literals
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib import admin
from django.forms import PasswordInput
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
import random
from datetime import datetime

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email
        and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email
        and password.
        """
        u = self.create_user(email, name=name, password=password)
        u.is_admin = True
        u.save(using=self._db)

        return u


class User(AbstractBaseUser):
    email = models.EmailField(
        db_column='useEmail',
        verbose_name='email address',
        max_length=255,
        unique=True,
        default='',
    )
    name = models.CharField(
        db_column='useName',
        max_length=100,
        default=''
    )
    created_at = models.DateTimeField(
        db_column='useDateJoined',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        db_column='useDateUpdate',
        auto_now=True
    )
    is_admin = models.BooleanField(
        db_column='useIsAdmin',
        default=False
    )
    is_active = models.BooleanField(
        db_column='useIsActive',
        default=False
    )   

    def tokens(self):
        tokens = RefreshToken.for_user(self)
        data = {
            'refresh': str(tokens),
            'access': str(tokens.access_token)
        }
        return data

    def get_full_name(self):
        # The user is identified by their email address
        return self.name

    def get_short_name(self):
        # The user is identified by their email address
        try:
            return self.name.split()[0]
        except:
            return ''

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_confirmed(self):
        return self.is_authenticated and self.active

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        managed = True
        db_table = 'User'


admin.site.register(User)