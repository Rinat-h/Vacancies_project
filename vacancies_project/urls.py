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
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import MyLoginView, MySignupView
from vacancies.views.my_company import CompanyCreate, CompanyUpdate, CompanyLetsstart
from vacancies.views.my_resume import MyResumeStart, MyResumeCreate, MyResumeUpdate
from vacancies.views.my_vacancies import MyVacanciesStart, MyVacanciesCreate, MyVacanciesList, MyVacanciesEdit, \
    VacancySend
from vacancies.views.views import MainView, VacanciesAllView, VacancyDetailView, CompanyDetailView, \
    VacanciesBySpeciality, \
    custom_handler404, custom_handler500, VacancySearch

handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', MainView.as_view(), name='MainView'),
    path('vacancies/', VacanciesAllView.as_view(), name='VacanciesAllView'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='VacancyDetailView'),
    path('vacancies/<str:code>/', VacanciesBySpeciality.as_view(), name='VacanciesBySpeciality'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='CompanyDetailView'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', MySignupView.as_view(), name='signup'),
    path('mycompany/letsstart/', CompanyLetsstart.as_view(), name='company_start'),
    path('mycompany/create/', CompanyCreate.as_view(), name='company_empty'),
    path('mycompany/', CompanyUpdate.as_view(), name='company_full'),
    path('mycompany/vacancies/letsstart/', MyVacanciesStart.as_view(), name='vacancy_start'),
    path('mycompany/vacancies/create/', MyVacanciesCreate.as_view(), name='vacancy_create'),
    path('mycompany/vacancies/', MyVacanciesList.as_view(), name='vacancy_list'),
    path('mycompany/vacancies/<int:pk>', MyVacanciesEdit.as_view(), name='vacancy_edit'),
    path('vacancies/<int:pk>/sent', VacancySend.as_view(), name='vacancy_send'),
    path('myresume/letsstart/', MyResumeStart.as_view(), name='resume_start'),
    path('myresume/create/', MyResumeCreate.as_view(), name='resume_create'),
    path('myresume/', MyResumeUpdate.as_view(), name='resume_edit'),
    path('search', VacancySearch.as_view(), name='vacancy_search')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
