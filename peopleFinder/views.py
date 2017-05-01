from django.views.generic import ListView, DetailView

from .forms import PeopleFinderForm
from .models import Person

# Create your views here.

class IndexView(ListView):
    template_name = 'peopleFinder/index.html'
    
    def get_form(self):
        if hasattr(self, 'form'):
            return self.form
        self.form = PeopleFinderForm(self.request.GET)
        return self.form

    def get_queryset(self):
        queryset = Person.objects.all()
        form = self.get_form()
        if form.is_valid():
            queryset = form.filter_queryset(queryset)
        return queryset

class PersonView(DetailView):
    model = Person
    template_name = 'peopleFinder/details.html'
