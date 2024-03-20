from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from .forms import LoginForm, RegisterForm

class LoginView(auth_views.LoginView):
    authentication_form = LoginForm
    template_name = 'accounts/login.html'

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    template_name = "accounts/register.html"
