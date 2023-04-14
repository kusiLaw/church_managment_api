from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def image_path(instance, filename):
  return 'members/image/'.format(instance.user.username, filename)

class Member(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  number = models.CharField(max_length=20, blank=True)
  occupation = models.CharField(max_length=45, blank=True)
  postal_code = models.CharField(max_length=20 )
  address_line = models.CharField(max_length=25)
  date_baptized = models.DateField(blank= True)
  image = models.ImageField(max_length=100, upload_to=image_path, null=True, blank= True )

  def __str__(self) -> str:
    return f'{self.user.first_name}  {self.user.last_name}'
  
  @property 
  def full_name(self):
    return self.__str__
  
  def has_full_membership(self) -> bool:
    '''
      Return True if a member is baptized.
      A member not fully baptized does not have full membership 
      permission  
    '''
    return self.date_baptized != None

class Dues_Register(models.Model):
  type= models.CharField(max_length=45, unique= True)
