from django.contrib import admin
from django.urls import path
from statusApi.views import StatusUpdateView

urlpatterns = [
path("status/<int:id>",StatusUpdateView.as_view())
]