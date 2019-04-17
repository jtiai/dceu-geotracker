from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import RouteLine, TrackedPoint


@admin.register(TrackedPoint)
class TrackedPointAdmin(OSMGeoAdmin):
    list_display = ("name", "location", "timestamp")
    list_filter = ("name",)

@admin.register(RouteLine)
class RouteLineAdmin(OSMGeoAdmin):
    list_display = ("name",)
