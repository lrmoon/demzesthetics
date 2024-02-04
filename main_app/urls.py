from django.urls import path

from . import views

urlpatterns = [
    path("2/", views.index, name='index'),
    path("", views.index2, name="index2")
]