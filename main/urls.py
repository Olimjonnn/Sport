from django.urls import path
from .views import *

urlpatterns = [
    path("", Index, name="index"),
    path("news/", News, name="news"),
    path("contact/", Contact, name="contact/")
]