# -*- coding:utf-8 -*-
from django.db import models


class Schedule(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    enabled = models.BooleanField(blank=True, default=True, db_index=True)
    last_modified = models.CharField(max_length=50, blank=True, null=True)
    content_length = models.BigIntegerField(blank=True, null=True)

    class Meta:
        app_label = 'main'

    def __unicode__(self):
        return self.name
