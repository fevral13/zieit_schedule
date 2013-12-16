# -*- coding:utf-8 -*-
from django import forms
from django.contrib.auth import authenticate, login


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label=u'Пароль', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not (email and password):
            return

        self.user = authenticate(username=email, password=password)
        if self.user is None:
            raise forms.ValidationError('Неверный email/пароль')
        return self.cleaned_data

    def save(self, request):
        login(request, self.user)