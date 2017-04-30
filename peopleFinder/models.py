from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    first = models.CharField(max_length=35)
    last = models.CharField(max_length=35)
    phone = models.CharField(max_length=10, default='0000000000') 
    email = models.EmailField(max_length=254, default='None')
    state = models.CharField(max_length=2, default='ZZ')

    def __str__(self):
        return "%s %s" %(self.first, self.last)

class Skill(models.Model):
    skill_name = models.CharField(max_length=35)
    person = models.ManyToManyField(Person, related_name="skill_set")

    def __str__(self):
        return self.skill_name

class Field(models.Model):
    field_name = models.CharField(max_length=35)
    person = models.ManyToManyField(Person, related_name="field_set")

    def __str__(self):
        return self.field_name
