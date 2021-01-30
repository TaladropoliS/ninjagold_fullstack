from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio),
    path('process_money', views.process_money),
    path('reset', views.reset),
]