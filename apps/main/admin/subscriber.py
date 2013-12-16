# -*- coding:utf-8 -*-
from django.contrib import admin

from main.models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('user', 'schedule')
    list_filter = ('schedule', )

admin.site.register(Subscriber, SubscriberAdmin)