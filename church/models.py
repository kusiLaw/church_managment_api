from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Common(models.Model):
  name = models.CharField(max_length=64, unique= True)
  
  class Meta:
    abstract = True
    ordering = ['name']
    indexes = [
      models.Index(fields=['name'])
    ]

  def __str__(self) -> str:
    return self.name

class Member(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  number = models.CharField(max_length=20, blank=True)
  occupation = models.CharField(max_length=45, blank=True)
  postal_code = models.CharField(max_length=20 )
  address_line = models.CharField(max_length=25)
  date_baptized = models.DateField(blank= True)
  image = models.ImageField(max_length=100, 
                  upload_to= lambda self, filename : f'file/{self.user.first_name}/{filename}',
                  null=True, blank= True )

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

class Dues(Common):
  pass

class Payment(models.Model):
  member = models.ForeignKey(Member, on_delete= models.CASCADE)
  dues = models.ForeignKey(Dues, on_delete=models.CASCADE)
  amount = models.DecimalField( max_digits=5, decimal_places=2)
  date = models.DateField( auto_now=False, auto_now_add=False)


class Department(Common):
  pass

class Leader(models.Model):
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  start_date = models.DateField()
  end_date = models.DateField()
