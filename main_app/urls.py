from django.urls import path

from . import views

urlpatterns = [
    path("", views.index2, name="index2"),
    path("team/", views.team, name="team")

]