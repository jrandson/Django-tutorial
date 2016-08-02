from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

'''
Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.
'''

# Create your models here.

#reiniciar o banco python manage.py makemigrations --kake-initial

class User(models.Model):
	pass

class Form(models.Model):
	description = models.CharField(max_length = 100,default='')
	data_cad = models.DateTimeField(default= timezone.now)

class Text_field(models.Model):	
	form = models.ForeignKey(Form, on_delete=models.CASCADE)
	
	name = models.CharField(max_length = 100)
	value = models.CharField(max_length = 150, default = '')
	


class Text_area(models.Model):
	form = models.ForeignKey(Form, on_delete=models.CASCADE)

	name = models.CharField(max_length = 100)
	value = models.TextField()
	

class Select_item(models.Model):
	
	form = models.ForeignKey(Form, on_delete = models.CASCADE)
	name = models.CharField(max_length=100)
	

class Item_field(models.Model):
	
	select_item = models.ForeignKey(Select_item, on_delete = models.CASCADE)
	name = models.CharField(max_length=100)
	selected = models.IntegerField(default=0)
	

