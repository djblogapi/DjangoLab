import uuid

import face_recognition
import numpy as np
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    face = models.ImageField(upload_to='faces', null=True, blank=True)
    # encoding = models.BinaryField(null=True, blank=True)
    encoding = ArrayField(base_field=models.FloatField(), null=True, blank=True)
    data = models

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
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)


@receiver(post_save, sender=File, )
def search_user(sender, instance, created, **kwargs):
    if created:
        image_path = instance.image.path
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]

        for user in User.objects.all():
            if face_recognition.compare_faces([encoding], np.array(user.encoding)):
                instance.user = user
                instance.save()
                break
