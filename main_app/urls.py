from django.urls import path

from . import views

urlpatterns = [
    path("", views.index2, name="index2"),
    path("2/", views.index, name='index'),
    path("team/", views.team, name="team"),
    path("services/", views.services, name="services"),

]