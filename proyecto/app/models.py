from django.db import models
from django.contrib.auth.models import User
from cities_light.models import City
from django.db.models.signals import post_save
# import fields



# Create your models here.

class DiaSemana(models.Model):
    nombre = models.CharField(max_length = 9)

    def __unicode__(self):
        return self.nombre

class Categoria(models.Model):
    title = models.CharField(max_length = 140)

    def __unicode__(self):
    	return self.title

# Snippet para extender la clase User
class UserProfile(models.Model):  
    user = models.OneToOneField(User)
    conocimientos = models.TextField()
    dias = models.ManyToManyField(DiaSemana)
    tiempo_de = models.TimeField(null=True)
    tiempo_a = models.TimeField(null=True)
    localidad = models.OneToOneField(City, null=True)


    def __str__(self):  
          return "%s's profile" % self.user  

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 

User.profile = property(lambda u: u.get_profile() )