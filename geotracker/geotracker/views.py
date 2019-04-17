import datetime

from django.contrib.gis.geos import LineString, Point
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View

from .forms import TrackingPointForm
from .models import TrackedPoint, RouteLine


class IndexView(TemplateView):
    """
    Show index view with a map and tracking buttons.
    """
    template_name = "geotracker/index.html"

    def get_context_data(self, **kwargs):
        context_data = super(IndexView, self).get_context_data(**kwargs)
        context_data["home_page"] = " active"
        return context_data


@method_decorator(csrf_exempt, name="dispatch")
class TrackingPointAPIView(View):
    """
    Handle simple API to post geolocation.
    """
    def post(self, request):
        form = TrackingPointForm(request.POST)

        if form.is_valid():
            tp = TrackedPoint()
            # Timestamp is in milliseconds
            tp.name = form.cleaned_data["name"]
            tp.timestamp = datetime.datetime.fromtimestamp(
                form.cleaned_data["timestamp"] / 1000
            )
            tp.location = Point(
                form.cleaned_data["longitude"], form.cleaned_data["latitude"]
            )
            tp.accuracy = form.cleaned_data["accuracy"]
            tp.altitude = form.cleaned_data["altitude"]
            tp.altitude_accuracy = form.cleaned_data["altitude_accuracy"]

            tp.save()

            return JsonResponse({"successful": True})
        return JsonResponse({"succesful": False, "errors": form.errors})


class TrackingPointsListView(View):
    """
    Show list of tracked locations with number of points.
    """
    def get(self, request):
        track_names = (
            TrackedPoint.objects.values("name")
            .distinct()
            .annotate(num_points=Count("name"))
            .values("name", "num_points")
        )

        return render(
            request,
            "geotracker/tracked_points_list.html",
            {"track_names": track_names, "tracked_page": " active"},
        )

class RouteCreateView(View):
    """
    Create a linestring from individual points.
    """
    def post(self, request):
        name = request.POST["name"]
        qs = TrackedPoint.objects.filter(name=name)
        # Create line
        points = [tp.location for tp in qs]
        linestring = LineString(points)
        RouteLine.objects.create(name=name, location=linestring)
        return redirect(reverse("routes-list"))


class RoutesListView(View):
    """
    List created linestrings.
    """
    def get(self, request):
        lines = RouteLine.objects.all()
        return render(
            request,
            "geotracker/tracked_routes.html",
            {"lines": lines, "tracked_lines_page": " active"},
        )
