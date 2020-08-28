from django.urls import path
from .views import (
    HomePageView,
    CheckPageView,
    PostDetailPageView,
)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('check/', CheckPageView.as_view(), name='check'),
    path('post_detail/<int:pk>', PostDetailPageView.as_view(), name='post_detail'),
]
