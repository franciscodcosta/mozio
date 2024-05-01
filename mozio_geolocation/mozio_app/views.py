from rest_framework import generics
from rest_framework.response import Response
from .models import Provider, ServiceArea
from .serializers import ProviderSerializer, ServiceAreaSerializer


class ProviderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaListCreateAPIView(generics.ListCreateAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class FindContainingPolygonsAPIView(generics.ListAPIView):
    serializer_class = ServiceAreaSerializer

    def list(self, request, *args, **kwargs):
        lat = request.query_params.get('lat')
        lng = request.query_params.get('lng')
        if lat is None or lng is None:
            return Response({"error": "Latitude and longitude must be provided as query parameters"}, status=400)

        polygons = ServiceArea.find_containing_polygons(lat, lng)
        serializer = self.serializer_class(polygons, many=True)
        return Response(serializer.data)
