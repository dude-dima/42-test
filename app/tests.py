from django.test import TestCase
from models import Customer


class SimpleTest(TestCase):

    def test_basic_addition(self):
        # A response
        response = self.client.get('/')
        # Check response status
        self.failUnlessEqual(response.status_code, 200)
        # Check page information
        customer = Customer.objects.get(pk=1)
        self.assertContains(response, customer.name, 1)
        self.assertContains(response, customer.surname, 1)
        self.assertContains(response, customer.bio, 1)
        self.assertContains(response, customer.contacts, 1)
