# -*- coding:utf-8 -*-
from django import forms

from main.models import Schedule, Subscriber


class SubscriptionForm(forms.Form):
    subscriptions = forms.ModelMultipleChoiceField(queryset=Schedule.objects.filter(enabled=True),
                                                   widget=forms.CheckboxSelectMultiple(),
                                                   required=False)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SubscriptionForm, self).__init__(*args, **kwargs)

    def save(self):
        new_subscriptions = set(self.cleaned_data['subscriptions'])
        old_subscriptions = set([i.schedule for i in Subscriber.objects.filter(user=self.user).only('schedule')])

        Subscriber.objects.filter(schedule__in=old_subscriptions - new_subscriptions, user=self.user).delete()
        for s in new_subscriptions - old_subscriptions:
            Subscriber.objects.create(user=self.user, schedule=s)
