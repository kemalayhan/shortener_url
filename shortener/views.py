from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import generics, mixins, permissions
from rest_framework.response import Response

from .serializers import UrlShortenerSerializer
from shortener.models import UrlShortener
from rest_framework_simplejwt.authentication import JWTAuthentication


class UrlShortenerCreateApiView(generics.CreateAPIView):
    serializer_class = UrlShortenerSerializer
    queryset = UrlShortener.objects.all()
    authentication_classes = [JWTAuthentication, SessionAuthentication,
                              BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class UrlShortenerApiView(generics.RetrieveAPIView):
    serializer_class = UrlShortenerSerializer
    queryset = UrlShortener.objects.all()
    lookup_field = 'short_url'

    def get(self, request, *args, **kwargs):
        short_url = self.kwargs['short_url']
        qs = UrlShortener.objects.filter(short_url__exact=short_url)
        if qs.count() != 1 and not qs.exists():
            return Response({"message": "Invalid short url"}, status=404)
        obj = qs.first()
        obj.clicks += 1
        obj.save()
        return Response({"url": obj.url}, headers={'location': ''}, status=302)
