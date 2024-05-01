from django.urls import path
from .views import ProviderListCreateAPIView, ServiceAreaListCreateAPIView, FindContainingPolygonsAPIView

urlpatterns = [
    path('providers/', ProviderListCreateAPIView.as_view(), name='provider-list-create'),
    path('service-areas/', ServiceAreaListCreateAPIView.as_view(), name='service-area-list-create'),
    path('find-polygons/', FindContainingPolygonsAPIView.as_view(), name='find-containing-polygons'),
]
