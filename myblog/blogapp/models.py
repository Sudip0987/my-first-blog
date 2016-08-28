from __future__ import unicode_literals

from django.db import models

class BlogPost(models.Model):
	author = models.CharField(max_length=40,null=True,blank=True)
	title = models.CharField(max_length=100)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	publish = models.BooleanField(default=False)
# Create your models here.
	def __str__(self):
		return self.title