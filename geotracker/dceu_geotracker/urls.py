from django.contrib import admin
from django.urls import path
from geotracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tracking-point/', views.TrackingPointAPIView.as_view(), name='tracking-point-api'),
    path('tracking-points-list/', views.TrackingPointsListView.as_view(), name='tracking-points-list'),
    path('route-create/', views.RouteCreateView.as_view(), name='route-create'),
    path('routes/', views.RoutesListView.as_view(), name="routes-list"),
    path('', views.IndexView.as_view(), name='tracking-index'),
]
