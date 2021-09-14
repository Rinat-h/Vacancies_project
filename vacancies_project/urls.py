"""vacancies_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from vacancies.views import MainView, VacanciesAllView, VacancyDetailView, CompanyDetailView, VacanciesBySpeciality, \
    custom_handler404, custom_handler500

handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', MainView.as_view(), name='MainView'),
    path('vacancies/', VacanciesAllView.as_view(), name='VacanciesAllView'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='VacancyDetailView'),
    path('vacancies/<str:code>/', VacanciesBySpeciality.as_view(), name='VacanciesBySpeciality'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='CompanyDetailView'),
]
