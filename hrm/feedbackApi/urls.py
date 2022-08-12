from django.contrib import admin
from django.urls import path

from feedbackApi.views import FeedbackView,FeedbackDetailView

urlpatterns = [
path("feedback",FeedbackView.as_view()),
path("feedback/<int:id>",FeedbackDetailView.as_view())

]



