# -*- coding:utf-8 -*-
import string
import random

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


def _generate_code():
    return ''.join((random.choice(string.ascii_lowercase) for _ in xrange(6)))


class PhoneVerificationManager(models.Manager):
    def verify(self, code):
        updated = self.filter(verification_code=code, used=False).update(used=True, used_datetime=now())
        return bool(updated)


class PhoneVerification(models.Model):
    user = models.ForeignKey(User)
    verification_code = models.CharField(max_length=6, unique=True, db_index=True)
    used = models.BooleanField(blank=True, default=False)
    used_datetime = models.DateTimeField(blank=True, null=True)

    objects = PhoneVerificationManager()

    class Meta:
        app_label = 'main'

    def __unicode__(self):
        return self.user

    def save(self, *args, **kwargs):
        if self.id is None:
            while True:
                code = _generate_code()
                try:
                    PhoneVerification.objects.get(verification_code=code)
                except PhoneVerification.DoesNotExist:
                    break

            self.verification_code = code
        super(PhoneVerification, self).save(*args, **kwargs)
