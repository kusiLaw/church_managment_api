from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
  username = None
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=32, null=False, blank=False)
  last_name = models.CharField(max_length=32, null=False, blank=False)

  class Meta:
        db_table = 'auth_user'

  @property
  def full_name(self):
    return f'{self.first_name} {self.last_name}'


def profile_path(self, filename):
  return f'church/static/profile/{self.user.username}/{filename}'
