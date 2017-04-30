from django.contrib import admin
from .models import Person, Field, Skill

# Register your models here.
admin.site.register(Person)
admin.site.register(Field)
admin.site.register(Skill)
