# -*- coding: utf-8 -*-
from django.urls import path
from django.views.decorators.cache import cache_page

from .views import GeoSearch

app_name = 'geoAPI'

#We are handling cache of the view for 24Hrs by DB cache for the  below URLs
urlpatterns = [
    path('get_address/<lat>/<lon>/',  cache_page(60 * 60 * 24)(GeoSearch.as_view()), name="geoSearch"),
    path('get_address/', cache_page(60 * 60 * 24)( GeoSearch.as_view()), name="geoSearch"),
]