from django.urls import path

from . import views

urlpatterns = [
    path("", views.index2, name="index2"),
    path("demi/", views.demi, name="demi"),
    path("yaz/", views.demi, name="yaz"),

]