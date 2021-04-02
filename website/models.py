from django.db import models

class Navigator(models.Model):
   website = models.CharField(max_length=255,blank=False,help_text='Enter alternative name')
   url = models.URLField(blank=False,help_text='Enter field link')
   
   def __str__(self):
       return self.website


