import django_tables2 as tables
from bus_route.models import Bus, Route, BusRoute


class BusTable(tables.Table):
    number_of_routes_this_bus_runs_on = tables.Column(accessor='get_routes_for_this_bus', linkify=True)
    class Meta:
        model = Bus
        fields = ['bus_name', 'bus_number', 'number_of_routes_this_bus_runs_on']

class RouteTable(tables.Table):
    numbers_of_buses_running_on_this_route = tables.Column(accessor='get_buses_on_this_roue', linkify=True)
    class Meta:
        model = Route
        fields = ['route_name', 'route_number', 'numbers_of_buses_running_on_this_route']


class RouteOfBus(tables.Table):
    class Meta:
        model = BusRoute
        fields = ['route__route_name', 'route__route_number', 'from_time', 'to_time']


class BusOnRoute(tables.Table):
    class Meta:
        model = BusRoute
        fields = ['bus__bus_name', 'bus__bus_number', 'from_time', 'to_time']

