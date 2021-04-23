# -*- coding: utf-8 -*-

import json

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core import signing

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CategorySerializer, CitySerializer, AdvertSerializer

from .forms import UserRegistrationForm
from .models import Advert, City, Category

# Create your views here.

class AdvertViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = [permissions.IsAdminUser]

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAdminUser]

def accountsRedirect(request):
    return HttpResponseRedirect(reverse("main_app:home"))

class homPageView(TemplateView):
    template_name="main_app/home.html"

class advertListView(ListView):
    def get_queryset(self):
        return Advert.objects.all().prefetch_related('city', 'category')

    def get(self, request, *args, **kwargs):
        object_list = self.get_queryset()
        data=serialize('json', object_list, cls=DjangoJSONEncoder)
        return JsonResponse({"data": json.loads(data)})

class advertDetailView(DetailView):
    model=Advert

    def get(self, request, *args, **kwargs):
        ob = self.get_object()
        ob.views+=1
        ob.save()
        data=serialize('json', (ob,), cls=DjangoJSONEncoder)
        return JsonResponse({"data": json.loads(data)[0]})

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
