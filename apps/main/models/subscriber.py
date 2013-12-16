# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Subscriber(models.Model):
    user = models.ForeignKey(User)
    schedule = models.ForeignKey('main.Schedule')

    def notify(self):
        pass

    class Meta:
        app_label = 'main'
        unique_together = ('user', 'schedule')

    def __unicode__(self):
        return unicode(self.user)