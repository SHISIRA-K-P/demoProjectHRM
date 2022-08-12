from django.contrib import admin
from django.urls import path
from .views import UserView,UserDetailView

urlpatterns = [
    path('users/accounts',UserView.as_view()),
    path('users/accounts/<int:id>',UserDetailView.as_view()),
]