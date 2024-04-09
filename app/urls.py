from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('optimize_me', views.optimize_me, name='optimize_me'),
]
