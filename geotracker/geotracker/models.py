import json
from django.contrib.gis.db import models


class TrackedPoint(models.Model):
    name = models.CharField(max_length=200)
    location = models.PointField(null=True, blank=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return "{} ({})".format(self.location.wkt, self.timestamp.isoformat())


class RouteLine(models.Model):
    name = models.CharField(max_length=200)
    location = models.LineStringField(null=True, blank=True)
    color = models.CharField(max_length=7, default="#a0a0a0")

    def get_geojson_feature(self):
        """
        Return self as GeoJSON feature instead of just plain geometry
        """

        return json.dumps(
            {
                "type": "Feature",
                "geometry": json.loads(self.location.geojson),
                 "properties": {"color": self.color},
            }
        )

    @property
    def route_length(self):
        l = self.location.transform(3857, clone=True)
        return l.length
