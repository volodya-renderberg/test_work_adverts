from django.urls import path
# from django.views.generic import TemplateView

from . import views

app_name = 'main_app'
urlpatterns = [
    # path('', views.home, name='home'),
    # path('', TemplateView.as_view(template_name="main_app/home.html"), name='home'),
    path('', views.homPageView.as_view(), name='home'),
]