from django.contrib import admin
from django.urls import path
from loginApi.views import SignInView

urlpatterns = [
path("users/accounts/login",SignInView.as_view())
]