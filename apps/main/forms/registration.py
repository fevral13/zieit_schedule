# -*- coding:utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string

from main.models import UserProfile


class RegistrationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label=u'Пароль', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'Пользователь с таким email уже есть')

        return email

    def save(self, request):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        u = User.objects.create_user(username=email, email=email, password=password)
        UserProfile.objects.create(user=u)

        user = authenticate(username=email, password=password)
        login(request, user)

        body = render_to_string('emails/greeting.html', {'user': user, 'password': password, 'request': request})
        send_mail(u'Подтверждение регистрации', body, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[email, ], fail_silently=False)