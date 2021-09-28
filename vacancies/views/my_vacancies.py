from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView


class MyVacanciesList(ListView):
    pass


class MyVacanciesEmptyForm(ListView):
    pass


class MyVacancyFullForm(DetailView):
    pass