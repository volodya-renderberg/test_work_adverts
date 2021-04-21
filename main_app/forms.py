# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.password_validation import validate_password

class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,validators=[validate_password])
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        required=('email',)