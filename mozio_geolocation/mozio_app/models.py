from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point


class Provider(gis_models.Model):
    class Meta:
        app_label = 'mozio_app'

    name = gis_models.CharField(max_length=100)
    email = gis_models.EmailField()
    phone_number = gis_models.CharField(max_length=20)
    language = gis_models.CharField(max_length=50)
    currency = gis_models.CharField(max_length=10)


class ServiceArea(gis_models.Model):
    class Meta:
        app_label = 'mozio_app'

    name = gis_models.CharField(max_length=100)
    price = gis_models.DecimalField(max_digits=10, decimal_places=2)
    area = gis_models.PolygonField()

    @classmethod
    def find_containing_polygons(cls, lat, lng):
        point = Point(lng, lat)
        containing_polygons = cls.objects.filter(area__contains=point)
        return containing_polygons
