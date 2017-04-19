from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.

class People(models.Model):
    first_name = models.CharField(max_length = 35)
    last_name = models.CharField(max_length = 35)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$') 
    email_address = forms.EmailField()
