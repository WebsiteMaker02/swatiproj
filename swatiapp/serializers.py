from rest_framework import serializers

from .models import Dynamic


class DynamicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dynamic
        fields = ('number', 'Context','Details')