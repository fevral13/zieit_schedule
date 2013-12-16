# -*- coding:utf-8 -*-

from django.contrib import messages
from django.shortcuts import render, redirect

from main.forms.subscription import SubscriptionForm
from main.models import Subscriber


def index(request):
    if request.user.is_authenticated():

        initial = {'subscriptions': Subscriber.objects.filter(user=request.user).values_list('schedule', flat=True)}
        form = SubscriptionForm(user=request.user,
                                initial=initial,
                                data=request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, u'Подписки сохранены')
            return redirect(request.path)

        return render(request, 'index-logged-in.html', {
            'form': form
        })

    else:
        return render(request, 'index.html')
