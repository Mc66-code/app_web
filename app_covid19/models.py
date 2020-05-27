from django.db import models

# Create your models here.
class Passion(models.Model):
  #  nom = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/")
    
  #  def __unicode__(self):
   #     return self.nom