# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email_verified = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    phone_verified = models.CharField(max_length=20, blank=True)

    class Meta:
        app_label = 'main'

    def __unicode__(self):
        return self.user

    def phone_is_verified(self):
        return self.phone and self.phone == self.phone_verified

    def email_is_verified(self):
        return self.user.email == self.email_verified

