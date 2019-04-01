from django.contrib import admin
from django.urls import path
from geotracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='tracking-index'),
]
