from django.db import models
from django.urls import reverse


class Manifesto(models.Model):
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Manifesto'
        verbose_name_plural = 'Manifestos'


class Press(models.Model):
    content =models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Press'
        verbose_name_plural = 'Press Entries'
