from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from shortener.models import UrlShortener


class UrlShortenerSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = UrlShortener
        fields = [
            'url',
            'short_url',
            'created',
            'clicks'
        ]
        read_only_fields = ['short_url', 'created', 'clicks']

    def get_short_url(self, obj):
        return f'localhost:8000/urls/s/{obj.short_url}'




