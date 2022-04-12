from django.db import models
from django.contrib.auth.models import User

"""
class CustomManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(text = "chess")   """
		
# Create your models here.

class Topic(models.Model):
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add = True)
	owner = models.ForeignKey(User,on_delete = models.CASCADE)
	
#	objects = models.Manager() #default
#	hellos = CustomManager() # custom
	def __str__(self):
		return self.text
		
class Entry(models.Model):
	topic = models.ForeignKey(Topic ,on_delete = models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)
	class meta:
		verbose_name_plural = "Entries"
	def __str__(self):
		return self.text[:50] + "..."
	
		

	



