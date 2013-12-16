# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from main.forms.login import LoginForm


def login(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        form.save(request)
        return redirect('index')

    return render(request, 'registration.html', {'form': form, 'action': u'Вход'})