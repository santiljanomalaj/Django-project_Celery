from django.test import TestCase
#from .views import InjectDataView
from django.urls import reverse
import logging

# Create your tests here.


class ViewsTestCase(TestCase):
    def test_init_load(self):
        """Initial Loading Test"""
        response = self.client.post(reverse('inject_data'))
        #print(response.json())
        self.assertEqual(response.json()['error'], "No file attached")
