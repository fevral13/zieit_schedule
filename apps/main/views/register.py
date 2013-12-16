# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect

from main.forms.registration import RegistrationForm


def register(request):
    form = RegistrationForm(request.POST or None)

    if form.is_valid():
        form.save(request)
        return redirect('index')

    return render(request, 'registration.html', {'form': form, 'action': u'Регистрация'})