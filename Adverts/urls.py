"""Adverts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.contrib.staticfiles import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from main_app.views import accountsRedirect, ProfileView, UserRegistrationView, UserProfileUpdateView

from main_app import views as main_views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'adverts', main_views.AdvertViewSet)
router.register(r'categories', main_views.CategoryViewSet)
router.register(r'cities', main_views.CityViewSet)

urlpatterns = [
    path('', include('main_app.urls')),
    path('api/', include(router.urls)),
    path('api/advert-list/', main_views.advertListView.as_view(), name='advert_list'),
    path('api/advert/<int:pk>/', main_views.advertDetailView.as_view(), name='advert_detail'),
    path('admin/', admin.site.urls),
    path('accounts/', accountsRedirect, name='accounts'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('accounts/registration/', UserRegistrationView.as_view(), name='registration'),
    path('accounts/profile/edit/', UserProfileUpdateView.as_view(), name='edit_profile'),
    # path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += staticfiles_urlpatterns()