from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View

from vacancies.forms import CompanyForm
from vacancies.models import Company


class CompanyLetsstart(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        if Company.objects.filter(owner=request.user):
            return redirect('company_full')
        else:
            return render(request, 'vacancies/company-create.html')


class CompanyCreate(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'vacancies/company-edit.html', context={
            'form': CompanyForm,
        })

    def post(self, request):
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            company.save()
            messages.success(request, 'Вы создали компанию!')
            return redirect('company_full')
        return render(request, 'vacancies/company-edit.html', context={
            'form': form,
        })


class CompanyUpdate(LoginRequiredMixin, View):

    def get(self, request):
        company = get_object_or_404(Company, owner=request.user)
        form = CompanyForm(instance=company)
        return render(request, 'vacancies/company-edit.html', context={
            'form': form,
        })

    def post(self, request):
        company = get_object_or_404(Company, owner=request.user)
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            company.save()
            messages.success(request, 'Информация о компании обновлена')
            return redirect('company_full')
        return render(request, 'vacancies/company-edit.html', context={
            'form': form,
        })
