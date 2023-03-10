from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('/signin',views.signin, name="signin_page"),
    path('/signup',views.signup, name="signup_page"),
    path('/logout',views.sign_out, name="logout")
]
