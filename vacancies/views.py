from django.db.models import Count
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from vacancies.models import Vacancy, Specialty, Company


def custom_handler404(request, exception):
    return HttpResponseNotFound('Извините, проект еще в доработке')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера....Починим как только так сразу!')


class MainView(TemplateView):
    template_name = "vacancies/index.html"

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['vacancies_by_specialty'] = Specialty.objects.annotate(num_vacan=Count('vacancies'))
        context['vacancies_by_company'] = Company.objects.annotate(num_vacan=Count('companies'))
        return context


class VacanciesAllView(ListView):
    model = Vacancy
    template_name = 'vacancies/vacancies.html'
    context_object_name = 'vacancies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Все вакансии'
        return context


class VacanciesBySpeciality(ListView):
    model = Vacancy
    template_name = 'vacancies/vacancies.html'
    context_object_name = 'vacancies'
    pk_url_kwarg = 'code'

    def get_queryset(self):
        self.specialty = get_object_or_404(Specialty, code=self.kwargs['code'])
        return Vacancy.objects.filter(specialty=self.specialty)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = self.specialty.title
        return context


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancies/vacancy.html'
    context_object_name = 'vacancy'


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'vacancies/company.html'
    context_object_name = 'company'


