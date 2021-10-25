from django.core.management import BaseCommand
from django.shortcuts import get_object_or_404

from vacancies import data
from vacancies.models import Vacancy, Company, Specialty


class Command(BaseCommand):

    def handle(self, *args, **options):

        for company in data.companies:
            new_company = Company(
                name=company['title'],
                location=company['location'],
                description=company['description'],
                employee_count=company['employee_count'],
            )
            new_company.save()

        for specialty in data.specialties:
            new_specialty = Specialty(
                code=specialty['code'],
                title=specialty['title'],
            )
            new_specialty.save()

        for job in data.jobs:
            vacancy = Vacancy(
                title=job['title'],
                salary_min=job['salary_from'],
                salary_max=job['salary_to'],
                published_at=job['posted'],
                skills=job['skills'],
                description=job['description'],
            )
            vacancy.save()
            vacancy.company.add(get_object_or_404(Company, pk=job['company']))
            vacancy.specialty.add(get_object_or_404(Specialty, code=job['specialty']))
