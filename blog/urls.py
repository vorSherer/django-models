from django.urls import path
from .views import HomePageView, CheckPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('check/', CheckPageView.as_view(), name='check'),
]
