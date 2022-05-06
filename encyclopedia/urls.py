from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>/", views.entrypage, name="entry"),
    path("search", views.searchpage, name="search"),
    path("newpage/", views.newpage, name="newpage"),
    path("save", views.savepage, name="savepage"),
]
