from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('',HomeView.as_view()),

    path('accounts/register', RegisterView.as_view()),
    path('accounts/login', LoginView.as_view(next_page="/")),
    path('accounts/logout', LogoutView.as_view(next_page="/")),


]