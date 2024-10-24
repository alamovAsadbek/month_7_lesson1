from cities_light.models import City
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Superusers must have an email address'))

        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserModel(BaseModel, AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name=_('Email'))
    avatar = models.ImageField(upload_to="users/", null=True, blank=True, verbose_name=_('Avatar'))

    company = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Company'))
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Phone'))

    address = models.TextField(verbose_name=_('Address'))
    zip_code = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Zip Code'))

    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('City'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
