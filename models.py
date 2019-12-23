from django.db import models

# Create your models here.
class ppl(models.Model):
    
    full_name = models.CharField(max_length=256,unique=True)
    username =  models.CharField(max_length=256,unique=True)
    pwd =  models.CharField(max_length=256)
    REQUIRED_FIELDS = ['full_name']
    USERNAME_FIELD='username'
    is_anonymous=False
    is_authenticated = False
    
    
   
    def __str__(self):
        return self.full_name

class blogpost(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    def __str__(self):
        return self.title
