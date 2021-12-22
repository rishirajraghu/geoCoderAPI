from rest_framework.views import APIView
from rest_framework.response import Response

from api.utils import get_nominatim_data


class GeoSearch(APIView):
    """
    Performs the reverse geo coding and returns name  of submitted location
    API GET method is capable of handling requests args passed as query params or even as URL position args in the format - myapp/get_address/<latitude>/<longitude>/
    
    Args:
        latitude : latitude of the location to be fetched from Nominatim
        longitude : latitude of the location to be fetched from Nominatim
        
    Returns:
        name : Location name of the latitude and longitude called
    """

    def get(self, request, format=None, **kwargs):

        #This view cam handle GET request in both URL params passed as well as query params
        lat = request.GET.get('lat') if request.GET.get('lat') is not None else kwargs.get('lat', None)
        lon = request.GET.get('lon') if request.GET.get('lon') is not None else kwargs.get('lon', None)

        #Return error response if latitude or longitude is not passed as args
        if lat is None :
            response = {"lat": "Parameter is missing"}
            return Response(response, status=404)
        if lon is None:
            response = {"lon": "Parameter is missing"}
            return Response(response, status=404)

        #Call the nominatim data fetching function
        nom_data = get_nominatim_data(lat=lat, lon=lon)

        return Response({'name' : nom_data.json()['display_name']} ,status=200)