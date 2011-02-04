from django.contrib.auth.models import User
from django.test import TestCase
from django.core.management import call_command
import sys
from StringIO import StringIO
from models import Customer


class SimpleTest(TestCase):
    # Load a fixture
    fixtures = ['init.xml']

    def test_contacts(self):
        # A response
        response = self.client.get('/')
        # Check response status
        self.failUnlessEqual(response.status_code, 200)
        # Check if used right template
        self.assertTemplateUsed(response, 'contacts.html', msg_prefix='')
        # Get an user
        customer = response.context['customer']
        c = Customer.objects.all()[0]
        # Check model parameters
        self.failUnlessEqual(c.name, customer.name)
        self.failUnlessEqual(c.surname, customer.surname)
        self.failUnlessEqual(c.bio, customer.bio)
        self.failUnlessEqual(c.contacts, customer.contacts)

    def test_requests(self):
        # A response
        response = self.client.get('/requests/')
        # Check response status
        self.failUnlessEqual(response.status_code, 200)
        # Check if used right template
        self.assertTemplateUsed(response, 'requests.html', msg_prefix='')

    def test_context_processor(self):
        # A response
        response = self.client.get('/')
        # Check if context contains project settings
        self.failUnlessEqual(response.context['settings'].SECRET_KEY, \
            '160-wua)ph_%rb16rrypkm8%%^)oj^rggnts#e8)8$c0(@httn')

    def test_edit(self):
        # A response
        response = self.client.get('/edit/')
        # Check response status before auth
        self.failUnlessEqual(response.status_code, 302)

        #Authorization
        User.objects.create_user(username="test",
                                 email="test@test.com",
                                 password="test")
        self.failUnlessEqual(self.client.login(username="test",
                                               password="test"), True)

        # A response
        response = self.client.get('/edit/')
        # Check response status after auth
        self.failUnlessEqual(response.status_code, 200)

        # Customer data before changing (commiting form)
        data = ['Dmitry', 'Razumov', "Some bio", "380500000000", "1983-07-12"]
        # Following data should be in the reponse content
        for item in data:
            self.failUnlessEqual(item in response.content, True)
        ctx = {'name': 'test1', 'surname': 'test2', 'contacts': 'test3',
               'bio': 'test4', 'birth_date': '1901-01-01'}
        # Emulating form submitting
        self.client.post('/edit/', ctx)
        response = self.client.get('/edit/')
        # Check response status
        self.failUnlessEqual(response.status_code, 200)
        # Customer data before changing (commiting form)
        data = ['test1', 'test2', "test3", "test4", "1901-01-01"]
        # Following data should be in the reponse content
        for item in data:
            self.failUnlessEqual(item in response.content, True)

    def test_reversed(self):
        #Authorization
        User.objects.create_user(username="test",
                                 email="test@test.com",
                                 password="test")
        self.failUnlessEqual(self.client.login(username="test",
                                               password="test"), True)
        # A response
        response = self.client.get('/edit/')
        # Check response status after auth
        self.failUnlessEqual(response.status_code, 200)
        # Check if fields was reversed
        self.failIf(response.content.index('id="id_name"') <
                    response.content.index('id="id_bio"'))

    def test_tag(self):
        # A response
        response = self.client.get('/tag/')
        # Check response status after auth
        self.failUnlessEqual(response.status_code, 200)

    def test_modelsinfo(self):
        temp = sys.stderr
        sys.stderr = stderr = StringIO()
        call_command('modelsinfo')
        sys.stderr = temp
        test_string = "<class 'django.contrib.auth.models.User'> " +\
                      "contains 1 objects"
        self.assertTrue(test_string in stderr.getvalue())
