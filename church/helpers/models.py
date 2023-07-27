from django.db import models

class Common(models.Model):
  create_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    abstract = True
    ordering = ['-create_at']


  def __str__(self) -> str:
    return NotImplemented