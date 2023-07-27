from django.db import models

class Common(models.Model):
  create_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    abstract = True
    ordering = ['-create_at']


  def __str__(self) -> str:
    return NotImplemented
  

def profile_path(name, filename):
  return f'church/static/profile/{name}/{filename}'



__all__ = ['Common', 'profile_path']