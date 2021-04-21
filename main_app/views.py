# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core import signing

from .forms import UserRegistrationForm

# Create your views here.

def accountsRedirect(request):
    return HttpResponseRedirect(reverse("main_app:home"))

class homPageView(TemplateView):
    template_name="main_app/home.html"

class ProfileView(LoginRequiredMixin, DetailView):
    template_name="main_app/profile_view.html"
    
    def get_object(self):
        return self.request.user

class UserRegistrationView(CreateView):
    template_name="registration/registration.html"
    model=User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        # if self.model.objects.filter(username=form.instance.username).count():
        #     form.add_error('username', 'Already exists!')
        #     return super().form_invalid(form)
        instance=form.instance
        del instance.__dict__['_state']
        user=User.objects.create_user(**instance.__dict__)
        login(self.request, user)
        return redirect(self.success_url)

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name="registration/edit_profile.html"
    model=User
    success_url = reverse_lazy("profile")
    fields=['email', 'first_name', 'last_name']

    def get_object(self):
        return self.request.user

    def post(self, *args, **kwargs):
        if 'cansel' in self.request.POST:
            return HttpResponseRedirect(self.success_url)
        else:
            return super().post(*args, **kwargs)