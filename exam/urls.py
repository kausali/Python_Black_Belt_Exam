from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.user_app.urls', namespace = "users")),
    url(r'^', include('apps.travel_app.urls', namespace = "travel")),
]
