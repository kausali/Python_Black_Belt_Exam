from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^travels$', views.success, name="success"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^home$', views.home, name="home"),
    url(r'^travels/add$', views.create, name="create"),
    url(r'^add_trip$', views.add_trip , name="add_trip"),
    url(r'^travels/destination/(?P<id>\d+)$', views.trip_detail, name = "item_detail"),
    url(r'^move_up/(?P<id>\d+)$', views.move_up, name = "move_up"),
]
