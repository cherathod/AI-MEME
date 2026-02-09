from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.MemeGeneratorView.as_view()),
]