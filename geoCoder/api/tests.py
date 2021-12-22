from django.test import TestCase, override_settings
from django.db import connection
from api.views import GeoSearch

class TestGeoAPI(TestCase):
	"""
    Tests for different API functionalities
    
    """

	def test_nominatim_call(self):
		response = self.client.get("/myapp/get_address/-35.4391708/-58.7064573/")
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data['name'], "Partido de Monte, Buenos Aires, Argentina")
