from django.urls import path
# from django.views.generic import TemplateView

from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.homPageView.as_view(), name='home'),
    path('advert-list/', views.advertListView.as_view(), name='advert_list'),
    path('advert/<int:pk>/', views.advertDetailView.as_view(), name='advert_detail'),
]