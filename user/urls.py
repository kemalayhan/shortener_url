from django.urls import path

from .views import RegisterAPIView, AuthAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    # path('login/', AuthAPIView.as_view(), name='login'),
]
