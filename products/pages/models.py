from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class ContactModel(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    subject = models.CharField(max_length=100, verbose_name=_('Subject'))

    message = models.TextField(verbose_name=_('Message'))
    email = models.EmailField(verbose_name=_('Email'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
