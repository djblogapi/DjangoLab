import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from user.managers import UserManager


class User(AbstractUser):
    """
    Extends Abstract User model with additional fields.
    Makes authentication with email and password fields.
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(_('Username'), max_length=150, null=True)
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    email = models.EmailField(_('Email'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f'{self.email}, {self.username}'

    def clean(self):
        self.email = self.email.strip().lower()
        super().clean()


class File(models.Model):
    image = models.ImageField(
        _("image"),
        upload_to="images",
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)

