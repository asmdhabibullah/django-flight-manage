from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from airport.models import Airport, Runway, Surface
from rest_framework.response import Response
from airport.serializers import AirportSerializer, RunwaySerializer, SurfaceSerializer


# Airports data getter and setter
#Airport.
class AirportViews(APIView):

    # Get all airport
    def get(self, request, format=None):
        try:
            airport = Airport.objects.all()
            serializer = AirportSerializer(airport, many=True)
            if len(serializer.data) > 0:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(data="Departments not found :(", status=status.HTTP_404_NOT_FOUND)
        except Airport.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    # Create new airport
    def post(self, request, format=None):
        serializer = AirportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Airport details.
class AirportDetailsViews(APIView):
    
    # Single airport
    def get_airport(self, pk):
        try:
            airport = Airport.objects.get(pk=pk)
            return airport
        except Airport.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Airports = self.get_airport(pk)
        return Response(Airports, status=status.HTTP_200_OK)

    # Update existing airport
    def put(self, request, pk, format=None):
        Airport = self.get_airport(pk)
        serializer = AirportSerializer(Airport, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_426_UPGRADE_REQUIRED)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete existing airport
    def delete(self, request, pk, format=None):
        airport = self.get_airport(pk)
        if airport:
            airport.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


# Runways
class RunwayViews(APIView):

    # All runway
    def get(self, request, format=None):
        try:
            runway = Runway.objects.all()
            serializer = RunwaySerializer(runway, many=True)
            if len(serializer.data) > 0:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(data="Runway not found :(", status=status.HTTP_404_NOT_FOUND)
        except Runway.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    # Create new one
    def post(self, request, format=None):
        serializer = RunwaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Runway details.
class RunwayDetailsViews(APIView):
    
    # Get single one
    def get_runways(self, pk):
        try:
            airport = Runway.objects.get(pk=pk)
            return airport
        except Runway.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        runway = self.get_runways(pk)
        return Response(runway, status=status.HTTP_200_OK)

    # Update single one
    def put(self, request, pk, format=None):
        runway = self.get_runways(pk)
        serializer = RunwaySerializer(runway, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_426_UPGRADE_REQUIRED)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete single one
    def delete(self, request, pk, format=None):
        runway = self.get_runways(pk)
        if runway:
            runway.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


# Surface
class SurfaceViews(APIView):
    
    # All surface
    def get(self, request, format=None):
        try:
            surface = Surface.objects.all()
            serializer = SurfaceSerializer(surface, many=True)
            if len(serializer.data) > 0:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(data="Surface not found :(", status=status.HTTP_404_NOT_FOUND)
        except Surface.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    # Add ne one
    def post(self, request, format=None):
        serializer = SurfaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Surface details.
class SurfaceDetailsViews(APIView):
    
    # Get single one
    def get_surfaces(self, pk):
        try:
            airport = Surface.objects.get(pk=pk)
            return airport
        except Surface.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        surface = self.get_surfaces(pk)
        return Response(surface, status=status.HTTP_200_OK)

    # update single one
    def put(self, request, pk, format=None):
        surface = self.get_surfaces(pk)
        serializer = SurfaceSerializer(surface, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_426_UPGRADE_REQUIRED)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete single one
    def delete(self, request, pk, format=None):
        surface = self.get_ss(pk)
        if surface:
            surface.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)