from django.urls import path, include
# from django.views.generic import TemplateView

from . import views

app_name = 'main_app'
urlpatterns = [
	path('', views.homPageView.as_view(), name='home'),
]