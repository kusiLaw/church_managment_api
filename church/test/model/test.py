from church.models import Membership
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.db import IntegrityError
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime 
from django.utils import timezone
from PIL import Image
import io



def create_user(username = 'law', password ='Test@password' ,
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
    user = create_user()
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
      create_user(first_name=None)
    

  def test_duplicate_email(self):
    '''
      create user fist name return IntegrityError 
    '''
    create_user(email='lawrence@yahoo.com')
    try:
      create_user(username='peter', email='lawrence@yahoo.com')
    except IntegrityError:
      pass


class MembershipTest(TestCase):
  """
    Test users who has membership
  """ 
  def setup(self, image = None, date_baptized= timezone.now(), delta=0):
    user = create_user()
    member = Membership.objects.create(user =user,date_baptized = date_baptized, postal_code ='mk4 6ny',
                                        address_line='6 raidon hub', number ='0742588635543', occupation='I.T', image =image)
    return member
    
  def test_create_membership(self):
    member = self.setup()
    self.assertEqual(member.date_baptized.date(),  timezone.now().date())
    self.assertEqual(member.number, "0742588635543")

  def test_create_membership_with_date_baptized_set_to_future(self):
    '''
      User can not have Membership with date baptized set to future 
    '''

    try:
      # set date_baptized 1 day ahead 
      self.setup(date_baptized = timezone.now() + datetime.timedelta(days = 1))
    except ValueError as e:
      self.assertEqual(str(e), 'Baptized date cant be in future') 

  def test_create_membership_without_baptized_date(self):
    '''
      User can have Membership without baptized date 
    '''
    member = self.setup(date_baptized = None)
    self.assertEqual(member.number, "0742588635543")
    self.assertEqual(member.postal_code, "mk4 6ny")
    
  def test_has_full_membership_with_no_baptized_date(self):
    '''
        A User with no baptized date is not a full member
    '''
    member = self.setup(date_baptized = None)

    self.assertFalse(member.has_full_membership())

  def test_create_membership_without_baptized_date(self):
    '''
      User can have Membership without baptized date 
    '''
    member = self.setup(date_baptized = None)
    self.assertEqual(member.number, "0742588635543")
    self.assertEqual(member.postal_code, "mk4 6ny")