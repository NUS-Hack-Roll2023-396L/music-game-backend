# from django.test import TestCase, Client
# from django.contrib.auth.models import User

# # Create your tests here.
# class AuthTestCase(TestCase):
#     client = Client()
    
#     def setUp(self):
#         User.objects.create_user('testuser', 'testuser@abc.com', 'testuser')
    
#     def test_list(self):
#         response = self.client.get('/auth/users/')
#         assert response.status_code == 200
#         assert len(response.data) == 1
        
#         user = response.data[0]
#         assert user['username'] == 'testuser'
#         assert user['email'] == 'testuser@abc.com'
        
        
    
#     def test_registration(self):
#         newuser = {
#             'username': 'newuser',
#             'email': 'newuser@abc.com',
#             'password': 'newuser',
#             'confirm_password': 'newuser'
#         }
        
#         self.client.post('/auth/create_user/', newuser)
        
#         response = self.client.get('/auth/users/')
#         assert response.status_code == 200
#         assert len(response.data) == 2
#         assert User.objects.filter(username='newuser').exists()
