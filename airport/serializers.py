from rest_framework import serializers
from airport.models import Airport, Runway, Surface


# Runway data controller
class RunwaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Runway
        fields = ("__all__")

# Surface data controller
class SurfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surface
        fields = ("__all__")

# Airport data controller
class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ("__all__")