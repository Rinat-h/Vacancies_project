from django.db.models import Count
from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView

from vacancies.forms import ApplicationForm
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


class VacancyDetailView(CreateView):
    template_name = 'vacancies/vacancy.html'
    form_class = ApplicationForm
    success_url = 'sent'

    def get_context_data(self, **kwargs):
        kwargs['vacancy'] = get_object_or_404(Vacancy, pk=self.kwargs['pk'])
        kwargs['previous_page'] = self.request.META['HTTP_REFERER']
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        vacancy = get_object_or_404(Vacancy, pk=self.kwargs['pk'])
        form = ApplicationForm(self.request.POST)
        application_form = form.save(commit=False)
        application_form.save()
        application_form.user.add(self.request.user)
        application_form.vacancy.add(vacancy)
        return super().form_valid(form)


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'vacancies/company.html'
    context_object_name = 'company'

    def get_context_data(self, **kwargs):
        kwargs['previous_page'] = self.request.META['HTTP_REFERER']
        return super().get_context_data(**kwargs)


