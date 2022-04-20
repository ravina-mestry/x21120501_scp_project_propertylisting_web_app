from django.db import models

# Create your models here.

class User(models.Model):
    
    def __unicode__(self):
        return self.username, self.password, self.email
        
    username = models.CharField(
        max_length = 20,
        default = ''
    ) 
    
    password = models.CharField(
        max_length = 20,
        default = ''
    ) 
    
    email = models.EmailField(
        max_length = 20,
        default = ''
    )    