from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.

class Person(models.Model):
    first = models.CharField(max_length = 35)
    last = models.CharField(max_length = 35)
    phone = models.CharField(max_length = 10, default = '0000000000') 
    email = models.EmailField(max_length = 254, default = 'No Email Available')

    def __str__(self):
        return "%s %s" %(self.first, self.last)

class Skill(models.Model):
    skill_name = models.CharField(max_length = 35)
    person = models.ManyToManyField(Person, related_name = "skill_set")

    def __str__(self):
        return self.skill_name
