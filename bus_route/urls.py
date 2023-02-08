from django.urls import path
from bus_route.views import home_view, bus_list_view, route_list_view, route_of_bus_view, bus_on_route_view

app_name = 'bus_route'

urlpatterns = [
    path('', home_view, name='home'),
    path('buses/', bus_list_view, name='bus-list'),
    path('routes/', route_list_view, name='route-list'),
    path('bus/<int:bus_id>/routes/', route_of_bus_view, name='route-of-bus'),
    path('route/<int:route_id>/buses/', bus_on_route_view, name='buses-on-route'),
]
