# -*- coding:utf-8 -*-
from django.contrib import admin

from main.models import Schedule, Subscriber


class SubscriberInline(admin.TabularInline):
    model = Subscriber



class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'enabled', 'content_length', 'last_modified')
    list_filter = ('enabled', )
    inlines = (SubscriberInline, )

admin.site.register(Schedule, ScheduleAdmin)