from django.urls import path

from shortener.views import UrlShortenerCreateApiView, UrlShortenerApiView

# Path: core/shortener/urls.py

# add url patterns for the shortener app
urlpatterns = [
    path('s/<str:short_url>/', UrlShortenerApiView.as_view(), name='get_shortener'),
    path('create/', UrlShortenerCreateApiView.as_view(), name='create_list_shortener'),
]