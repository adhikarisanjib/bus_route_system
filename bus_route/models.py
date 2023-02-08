from django.db import models
from django.urls import reverse_lazy, reverse


class Route(models.Model):
    route_name = models.CharField(max_length=255)
    route_number = models.SmallIntegerField(unique=True)

    def get_buses_on_this_roue(self):
        return len(self.bus_set.all())

    def get_absolute_url(self):
        return reverse('bus_route:buses-on-route', args=(self.pk,))

    def __str__(self):
        return self.route_name

    
class Bus(models.Model):
    bus_name = models.CharField(max_length=255)
    bus_number = models.SmallIntegerField(unique=True)
    routes = models.ManyToManyField(to=Route, through="BusRoute")
    
    def __str__(self):
        return self.bus_name

    def get_routes_for_this_bus(self):
        return len(self.routes.all())

    def get_absolute_url(self):
        return reverse('bus_route:route-of-bus', args=(self.pk,))

    class Meta:
        verbose_name = 'bus'
        verbose_name_plural = 'buses'


class BusRoute(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()

    class Meta:
        unique_together = (("bus", "route", "from_time", "to_time"),)
