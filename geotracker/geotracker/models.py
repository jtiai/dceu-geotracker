import json

from django.contrib.gis.db import models
from django.core.validators import RegexValidator


class TrackedPoint(models.Model):
    name = models.CharField(max_length=200)
    location = models.PointField(null=True, blank=True)
    timestamp = models.DateTimeField()
    altitude = models.FloatField(blank=True, null=True)
    altitude_accuracy = models.FloatField(blank=True, null=True)
    accuracy = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "{} ({})".format(self.location.wkt, self.timestamp.isoformat())


class RouteLine(models.Model):
    name = models.CharField(max_length=200)
    location = models.LineStringField(null=True, blank=True)
    color = models.CharField(
        max_length=7, default="#a0a0a0", validators=[RegexValidator("#[a-fA-F0-9]{6}")],
        help_text="Use hexadecimal format like #a0a0a0"
    )

    def __str__(self):
        return self.name

    def get_geojson_feature(self):
        """
        Return self as GeoJSON feature instead of just plain geometry.

        Color property is used on a map to color geometry. Use only hexadecimal format.
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
        """
        Get length of the route.
        """
        geom = self.location.transform(3857, clone=True)
        return geom.length
