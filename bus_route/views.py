from django.shortcuts import render

from bus_route.models import Bus, Route, BusRoute
from bus_route.tables import BusTable, RouteTable, BusOnRoute, RouteOfBus


def home_view(request, *args, **kwargs):
    return render(request, 'bus_route/home.html')


def bus_list_view(request, *args, **kwargs):
    buses = BusTable(Bus.objects.all())
    context = {
        'table': buses,
    }
    return render(request, 'bus_route/bus_list.html', context)


def route_list_view(request, *args, **kwargs):
    routes = RouteTable(Route.objects.all())
    context = {
        'table': routes,
    }
    return render(request, 'bus_route/route_list.html', context)


def route_of_bus_view(request, bus_id, *args, **kwargs):
    bus_routes = RouteOfBus(BusRoute.objects.filter(bus__id = bus_id))
    context = {
        'table': bus_routes,
    }
    return render(request, 'bus_route/route_of_bus.html', context)


def bus_on_route_view(request, route_id, *args, **kwargs):
    route_buses = BusOnRoute(BusRoute.objects.filter(route__id = route_id))
    context = {
        'table': route_buses,
    }
    return render(request, 'bus_route/bus_on_route.html', context)
