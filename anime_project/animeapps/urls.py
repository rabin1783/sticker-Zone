from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name="user.home"),
    path('users/create/',views.registration,name="user.create"),
    path('users/login/',views.login,name="user.login"),
    path('users/login/naruto/',views.naruto,name="user.naruto"),
    path('users/logout/',views.user_logout,name="user.logout"),
    path('users/otp/',views.user_otp,name="user.otp")
]




