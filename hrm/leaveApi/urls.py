from django.contrib import admin
from django.urls import path

from leaveApi.views import LeaveView,LeaveDetailView

urlpatterns = [
path("leave",LeaveView.as_view()),
path("leave/<int:id>",LeaveDetailView.as_view())

]
