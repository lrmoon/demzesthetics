from django.urls import path

from . import views

urlpatterns = [
    path("", views.index2, name="index"),
    path("demi/", views.demi, name="demi"),
    path("yaz/", views.yaz, name="yaz"),

]