from django.test import TestCase
from models import User

class SimpleTest(TestCase):
    # Load a fixture
    fixtures = ['init.xml']
    def test_basic_addition(self):
        # A response
        response = self.client.get('/test42/main/')
        # Check response status
        self.failUnlessEqual(response.status_code, 200)
        # Check if used right template
        self.assertTemplateUsed(response, 'contacts.html', msg_prefix='')
        # Get an user
        user = response.context['user']
        u = User.objects.get(pk=1)
        # Check model parameters
        self.failUnlessEqual(u.name, user.name)
        self.failUnlessEqual(u.surname, user.surname)
        self.failUnlessEqual(u.bio, user.bio)
        self.failUnlessEqual(u.contacts, user.contacts)
        
        # A response
        response = self.client.get('/test42/requests/')
        # Check response status
        self.failUnlessEqual(response.status_code, 200)
        # Check if used right template
        self.assertTemplateUsed(response, 'requests.html', msg_prefix='')
        
        # A response
        response = self.client.get('/test42/main/')
        # Check if context contains project settings
        self.failUnlessEqual(response.context['settings'].SECRET_KEY, \
            '160-wua)ph_%rb16rrypkm8%%^)oj^rggnts#e8)8$c0(@httn')
        