from django.views.generic import TemplateView, DetailView, ListView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Counties, Shop
from django.core.serializers import serialize
from django.core import serializers
import json




class HomePageView(TemplateView):
    template_name = 'index.html'


def county_datasets(request):

	counties = serialize('geojson', Counties.objects.all())


	return HttpResponse(counties, content_type='json')



def shop_datasets(request):

	#shops = serialize('geojson', Shop.objects.all())

    data = serializers.serialize("geojson", Shop.objects.all())

    return HttpResponse(data, content_type='json')



class HomePageDetail(DetailView):
    """
        Shop detail view.
    """
    template_name = 'index.html'
    model = Shop


class ShopListView(ListView):

    template_name = 'listshops.html'
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.all()