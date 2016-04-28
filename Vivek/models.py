from __future__ import unicode_literals
from django.db import models

# Create your models here.
class SignUp(models.Model):
	first_name = models.CharField(max_length=120, blank=False, null=True)
	last_name = models.CharField(max_length=120, blank=False, null=True)
	email = models.EmailField()
	address1 = models.CharField(max_length=300, blank=False, null=True)
	address2 = models.CharField(max_length=300, blank=False, null=True)
	city = models.CharField(max_length=30, blank=False, null=True)
	zipcode = models.CharField(max_length=5, blank=False, null=True)
	phone_number = models.CharField(max_length=12, default= '123-456-7890', blank=False, null = False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.email