import requests

from django.conf import settings


REQUEST_ERROR_DATA = {
        "data":'API Unavailable', 
        "status_code": 404
}

def get_nominatim_data(lat, lon, url=settings.NOMINATIM_URL):
    """ 
    Function handles the Nominatim interaction

    Args :
        lat : Latitude of the location to be searched in Nominatim
        lat : Longitude of the location to be searched in Nominatim

    """

    #Params to be set for Nominatim call
    params = {}
    params["lat"] = float(lat)
    params["lon"] = float(lon)
    params["format"] = 'json'

    try:
        #Get the location data from nominatim by passing latitude and longitude
        nom_data = requests.get(url, params=params)
    except Exception:
        return REQUEST_ERROR_DATA

    if nom_data.status_code == 200:
        return nom_data

    return REQUEST_ERROR_DATA