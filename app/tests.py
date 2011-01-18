from django.contrib.auth.models import User
from django.test import TestCase
import tools

class SimpleTest(TestCase):
    # Load a fixture
    fixtures = ['init.xml']
    def test_basic_addition(self):
        # A response
        response = self.client.get('/main/')
        # Check response status
        self.failUnlessEqual(response.status_code, 200)
        # Check if used right template
        self.assertTemplateUsed(response, 'contacts.html', msg_prefix='')
        # Get an user
        user = response.context['customer']
        u = tools.get_default_customer()
        # Check model parameters
        self.failUnlessEqual(u.name, user.name)
        self.failUnlessEqual(u.surname, user.surname)
        self.failUnlessEqual(u.bio, user.bio)
        self.failUnlessEqual(u.contacts, user.contacts)
        
        # A response
        response = self.client.get('/requests/')
        # Check response status
        self.failUnlessEqual(response.status_code, 200)
        # Check if used right template
        self.assertTemplateUsed(response, 'requests.html', msg_prefix='')
        
        # A response
        response = self.client.get('/main/')
        # Check if context contains project settings
        self.failUnlessEqual(response.context['settings'].SECRET_KEY, \
            '160-wua)ph_%rb16rrypkm8%%^)oj^rggnts#e8)8$c0(@httn')
        
        # A response
        response = self.client.get('/edit/')
        # Check response status before auth
        self.failUnlessEqual(response.status_code, 302)
        
        #Authorization
        User.objects.create_user( username = "test",
                                  email = "test@test.com",
                                  password = "test")
        self.failUnlessEqual(self.client.login(username = "test",
                                               password = "test"), True)
        # A response
        response = self.client.get('/edit/')
        # Check response status after auth
        self.failUnlessEqual(response.status_code, 200)
        
        # Customer data before changing (commiting form)
        data = ['Dmitry', 'Razumov', "Some bio", "380500000000", "1983-07-12"]
        # Following data should be in the reponse content
        for item in data:
            self.failUnlessEqual(item in response.content, True)
        ctx = {'name':'test1', 'surname':'test2', 'contacts':'test3',
               'bio':'test4', 'birth_date':'1901-01-01'}
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
            
        # A response
        response = self.client.get('/edit/')
        # Check response status after auth
        self.failUnlessEqual(response.status_code, 200)
        # Check if fields was reversed
        self.failIf(response.content.index('id="id_name"') <
                    response.content.index('id="id_bio"'))
        
        # A response
        response = self.client.get('/tag/')
        # Check response status after auth
        self.failUnlessEqual(response.status_code, 200)
        