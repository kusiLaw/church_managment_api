from django.db import models
from django.utils import timezone
from datetime import datetime
from django.utils import timezone
from church.helpers.models import Common
from authentication.models import User
from church.helpers import Common, profile_path


class Membership(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  number = models.CharField(max_length=20, blank=True, null=True)
  occupation = models.CharField(max_length=45, blank=True, null=True)
  postal_code = models.CharField(max_length=20 )
  address_line = models.CharField(max_length=25)
  date_baptized = models.DateField(blank= True, null=True, help_text='Date Object. Helps to determined if a user is \
                                    considered as member of the church ')
  image = models.ImageField(max_length=100, 
                  upload_to= profile_path,
                  null=True, blank= True )

  def __str__(self) -> str:
    return f'{self.user.first_name}  {self.user.last_name}'

 
  def has_full_membership(self) -> bool:
    '''
      Return True if a member is baptized.
      A member not fully baptized does not have full membership 
      permission  
    '''
    return self.date_baptized != None

  def save(self, *args, **kwargs):

    if isinstance(self.date_baptized, datetime) and self.date_baptized > timezone.now():
      raise ValueError('Baptized date cant be in future')
    super(Membership, self).save(*args, **kwargs)


class Dues(Common):
  pass

class Payment(models.Model):
  member = models.ForeignKey(Membership, on_delete= models.CASCADE)
  dues = models.ForeignKey(Dues, on_delete=models.CASCADE)
  amount = models.DecimalField( max_digits=5, decimal_places=2)
  date = models.DateField( auto_now=False, auto_now_add=False)


class Department(Common):
  pass

class Leadership(models.Model):
  '''
      only member who are primarily baptized get leadership position
  '''
  member = models.ForeignKey(Membership, on_delete=models.CASCADE)
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  start_date = models.DateField()
  end_date = models.DateField()

class Event(models.Model):
  title = models.CharField(max_length=100)
  theme = models.CharField(max_length=100, null=True, blank=True , help_text='Theme of the event or church programs')
  image =models.ImageField(max_length=100, upload_to= 'church/static/events/')
  description = models.TextField()
  start_date = models.DateField()
  end_date = models.DateField()
  created_at = models.DateField(auto_now_add=True)
  location = models.CharField(max_length=100)
  speaker = models.CharField(max_length=100)
  guss_speaker = models.CharField(max_length=100)
  
  def __str__(self) -> str:
    return f'{self.title}  {self.speaker}  + {self.location} + {self.pk}'