from django.contrib import admin

#from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop, Counties

from leaflet.admin import LeafletGeoAdmin




class ShopAdmin(LeafletGeoAdmin):

    list_display = ('name', 'location')


class CountiesAdmin(LeafletGeoAdmin):

	list_display =('counties','codes')


admin.site.register(Shop, ShopAdmin)

admin.site.register(Counties, CountiesAdmin)