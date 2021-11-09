from os import name
from django.urls import path
from django.urls.conf import include
from .views import *
urlpatterns = [
    path('',login_view,name="login_view"),
    path('home/',home,name="home"),
    path('jsa_checklist/',jsa_checklist,name="jsa_checklist")
]
