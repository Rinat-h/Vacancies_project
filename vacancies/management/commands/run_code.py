from django.core.management import BaseCommand

from vacancies import data
from vacancies.models import Vacancy, Company, Specialty


class Command(BaseCommand):

    def handle(self, *args, **options):
        company_list = list()
        for company in data.companies:
            company_list.append(Company(
                name=company['title'],
                location=company['location'],
                description=company['description'],
                employee_count=company['employee_count']
            ))
        for company in company_list:
            company.save()

        specialty_list = list()
        for specialty in data.specialties:
            specialty_list.append(Specialty(
                code=specialty['code'],
                title=specialty['title']
            ))
        for specialty in specialty_list:
            specialty.save()

        # функция для получения нужного эземпляра класса specialty для связи ManytoMany
        def spec_by_vacan(specialty_from_vacan):
            for specialty in specialty_list:
                if specialty.code == specialty_from_vacan:
                    return specialty

        for job in data.jobs:
            vacancy = Vacancy(
                title=job['title'],
                salary_min=job['salary_from'],
                salary_max=job['salary_to'],
                published_at=job['posted'],
                skills=job['skills'],
                description=job['description']
            )
            vacancy.save()
            vacancy.company.add(company_list[int(job['company']) - 1])
            vacancy.specialty.add(spec_by_vacan(job['specialty']))
