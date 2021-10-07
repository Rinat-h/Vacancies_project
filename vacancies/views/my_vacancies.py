from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from vacancies.forms import VacancyForm
from vacancies.models import Vacancy, Company
from django.contrib import messages
import datetime


class MyVacanciesStart(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        company = Company.objects.filter(owner=request.user)
        if Vacancy.objects.filter(company__in=company):
            return redirect('vacancy_list')
        else:
            return render(request, 'vacancies/vacancy-create.html', context={
                'title': 'Создать вакансии'
            })


class MyVacanciesCreate(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'vacancies/vacancy-edit.html', context={
            'form': VacancyForm,
            'title': 'Вакансии компании'
        })

    def post(self, request):
        form = VacancyForm(request.POST)
        company = Company.objects.filter(owner=request.user)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.published_at = datetime.date.today()
            vacancy.save()
            vacancy.specialty.add(form.cleaned_data.get('specialty'))
            vacancy.company.add(company[0].pk)
            return redirect('vacancy_list')
        return render(request, 'vacancies/vacancy-edit.html', context={
            'form': form,
            'title': 'Вакансии компании'
        })


class MyVacanciesEdit(LoginRequiredMixin, View):

    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        speciality = vacancy.specialty.all().first()
        form = VacancyForm(instance=vacancy, initial={'specialty': speciality.pk})
        return render(request, 'vacancies/vacancy-edit.html', context={
            'form': form,
            'title': 'Вакансии компании',
            'vacancy_title': vacancy.title
        })

    def post(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        speciality = vacancy.specialty.all().first()
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            vacancy_form = form.save(commit=False)
            vacancy_form.published_at = datetime.date.today()
            vacancy_form.save()
            vacancy_form.specialty.remove(speciality)
            vacancy_form.specialty.add(form.cleaned_data.get('specialty'))
            messages.success(request, 'Информация о вакансии обновлена')
        return render(request, 'vacancies/vacancy-edit.html', context={
            'form': form,
            'title': 'Вакансии компании',
            'vacancy_title': vacancy.title
        })


class MyVacanciesList(LoginRequiredMixin, View):

    def get(self, request):
        company = Company.objects.filter(owner=request.user)
        vacancies = Vacancy.objects.filter(company__in=company)
        return render(request, 'vacancies/vacancy-list.html', context={
            'vacancies_list': vacancies,
            'title': 'Вакансии компании'
        })


class VacancySend(View):
    pass

