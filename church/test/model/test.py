from church.models import User
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.db import IntegrityError


def CreateUser(username = 'law', password ='Test@password' ,
                first_name = 'lawrence', last_name='kusi', email='test@gmail.com'):
  
  User = get_user_model() # return active user model or could import directly from ch.model  
  user = User.objects.create(username = username, password = password, 
                             first_name = first_name , last_name = last_name, email= email)
  return user

class CustomUserTest(TestCase):
  '''
    test custom user attribute and method
  '''
  def test_create_user(self):
    user = CreateUser()
    self.assertEqual(user.email,  'test@gmail.com')
    self.assertEqual(user.first_name, 'lawrence')
    self.assertEqual(user.full_name, 'lawrence kusi')
    self.assertTrue(user.is_active)
    self.assertFalse(user.is_superuser)

  def test_create_user_without_first_name(self):
    '''
      create user fist name return IntegrityError 
    '''
    with self.assertRaises(IntegrityError):
      CreateUser(first_name=None)
    

  def test_duplicate_email(self):
    '''
      create user fist name return IntegrityError 
    '''
    CreateUser(email='lawrence@yahoo.com')
    try:
      CreateUser(username='peter', email='lawrence@yahoo.com')
    except IntegrityError:
      pass

     
     