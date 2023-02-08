from django.contrib import admin

from bus_route.models import Bus, Route, BusRoute

admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(BusRoute)
