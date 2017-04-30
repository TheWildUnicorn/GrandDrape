from django import forms
from django.db.models import Q

from .models import Field, Skill

class PeopleFinderForm(forms.Form):
    name = forms.CharField(required=False)
    state = forms.CharField(required=False)
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(), required=False)
    field = forms.ModelChoiceField(queryset=Field.objects.all(),
                                   required=False)

    def filter_queryset(self, queryset):
        if self.cleaned_data['name']:
            name = self.cleaned_data['name']
            queryset = queryset.filter(Q(first__icontains=name) |
                                       Q(last__icontains=name))
        if self.cleaned_data['state']:
            state = self.cleaned_data['state']
            queryset = queryset.filter(state__icontains=state)

        if self.cleaned_data['skills']:
            skills = self.cleaned_data['skills']
            for skill in skills:
                queryset = queryset.filter(skill_set=skill)

        if self.cleaned_data['field']:
            field = self.cleaned_data['field']
            queryset = queryset.filter(field_set=field)

        return queryset
