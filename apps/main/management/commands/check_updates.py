# -*- coding:utf-8 -*-
import urllib2

from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.core.management import BaseCommand
from django.template.loader import render_to_string

from main.models import Schedule


class HeadRequest(urllib2.Request):
    def get_method(self):
        return 'HEAD'


class Command(BaseCommand):

    def handle(self, *args, **options):
        for schedule in Schedule.objects.filter(enabled=True):
            response = urllib2.urlopen(HeadRequest(schedule.url))

            last_modified = response.headers.dict['last-modified']
            content_length = response.headers.dict['content-length']
            initial_check = None in (schedule.last_modified, schedule.content_length)
            modified = unicode(schedule.content_length) != unicode(content_length)

            if initial_check or modified:
                schedule.last_modified = last_modified
                schedule.content_length = content_length
                schedule.save()

                if modified:
                    file_contents = urllib2.urlopen(schedule.url).read()
                    for subscriber in schedule.subscriber_set.all():
                        body = render_to_string('emails/notification.html', {'schedule': schedule})
                        email = EmailMessage(u'Расписание изменилось', body, settings.DEFAULT_FROM_EMAIL, [subscriber.user.email])
                        email.attach(schedule.url.split('/')[-1], file_contents, response.headers.dict['content-type'])
                        email.send()