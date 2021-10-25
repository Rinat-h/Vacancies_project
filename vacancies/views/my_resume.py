from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from vacancies.forms import ResumeForm
from vacancies.models import Resume


class MyResumeStart(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        if Resume.objects.filter(user=request.user):
            return redirect('resume_edit')
        else:
            return render(request, 'vacancies/resume-create.html', context={
                'title': 'Создать резюме'
            })


class MyResumeCreate(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'vacancies/resume-edit.html', context={
            'form': ResumeForm,
            'title': 'Создать резюме'
        })

    def post(self, request):
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.specialty = form.cleaned_data['specialty']
            resume.save()
            messages.success(request, 'Вы создали резюме!')
            return redirect('resume_edit')
        return render(request, 'vacancies/resume-edit.html', context={
            'form': form,
            'title': 'Создать резюме'
        })


class MyResumeUpdate(LoginRequiredMixin, View):

    def get(self, request):
        resume = get_object_or_404(Resume, user=request.user)
        form = ResumeForm(instance=resume)
        return render(request, 'vacancies/resume-edit.html', context={
            'form': form,
            'title': 'Редактировать резюме'
        })

    def post(self, request):
        resume = get_object_or_404(Resume, user=request.user)
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            resume_form = form.save(commit=False)
            resume_form.user = request.user
            resume_form.specialty = form.cleaned_data['specialty']
            resume_form.save()
            messages.success(request, 'Ваше резюме обновлено')
            return redirect('resume_edit')
        return render(request, 'vacancies/resume-edit.html', context={
            'form': form,
            'title': 'Редактировать резюме'
        })
