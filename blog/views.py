from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
)
from .models import Post


class HomePageView(ListView):
    template_name = 'home.html'
    model = Post


class CheckPageView(TemplateView):
    template_name = 'check.html'


