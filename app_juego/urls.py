from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio),
    path('process_money', views.process_money),
    path('granja', views.granja),
    path('cueva', views.cueva),
    path('casa', views.casa),
    path('casino', views.casino),
]