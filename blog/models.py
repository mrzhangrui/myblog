from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
	blog_name=models.CharField(max_length=50)
	user_name=models.CharField(max_length=50)
	content=models.CharField(max_length=200)
	create_at=models.DateField(auto_now_add=True)
	def __str__(self):
		return self.content

class Blog(models.Model):
	user_name=models.CharField(max_length=50)
	name=models.CharField(max_length=50)
	summary=models.CharField(max_length=50)
	content=models.CharField(max_length=500)
	create_at=models.DateField(auto_now_add=True)
	

	def __str__(self):
		return self.name

