from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url('', views.ShopListView.as_view(), name='list'),
    url(r'^city/(?P<pk>[0-9]+)$', views.HomePageDetail.as_view(), name='index'),
    url('county-data/', views.county_datasets, name="county"),
    url('shops-data/', views.shop_datasets, name="shop"),

]