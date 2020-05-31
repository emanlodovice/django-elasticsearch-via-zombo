from django.contrib.auth.models import User
from django.db import models

from django_zombodb.indexes import ZomboDBIndex
from django_zombodb.querysets import SearchQuerySet


class Archive(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name="archives",
        on_delete=models.CASCADE,
    )


class ArchiveZombo(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name="archives_zombo",
        on_delete=models.CASCADE,
    )

    objects = models.Manager.from_queryset(SearchQuerySet)()
    
    class Meta:
        indexes = [
            ZomboDBIndex(fields=[
                'content',
            ]),
        ]
