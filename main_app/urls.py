from django.urls import path, include
# from django.views.generic import TemplateView

from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'adverts', views.AdvertViewSet)

app_name = 'main_app'
urlpatterns = [
	path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
    # path('', views.homPageView.as_view(), name='home'),
    # path('advert-list/', views.advertListView.as_view(), name='advert_list'),
    # path('advert/<int:pk>/', views.advertDetailView.as_view(), name='advert_detail'),
]