from django.db import models

# Create your models here.

class User(models.Model):
    
    username = models.CharField(max_length=40)
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
 
    def __str__(self):
        return self.username+" "+self.email

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'