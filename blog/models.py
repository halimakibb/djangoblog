from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class Author(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField(blank=True)
	bio = models.TextField()
	
	def __unicode__(self):
		return self.name
	
class Category(models.Model):
	name = models.CharField(max_length = 50)
	description = models.CharField(max_length = 255)
	
	class Meta:
		verbose_name_plural = 'Categories'
	
	def __unicode__(self):
		return self.name	
	
class Tag(models.Model):
	name = models.CharField(max_length = 50)
	description = models.CharField(max_length = 255)
	
	def __unicode__(self):
		return self.name	

class Post(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	updated = models.DateTimeField(default=datetime.now, blank=True)
	body = models.TextField()
	author = models.ForeignKey(Author)
	categories = models.ManyToManyField(Category)
	tags = models.ManyToManyField(Tag)
	
	def __unicode__(self):
		return self.title
	
	
	


