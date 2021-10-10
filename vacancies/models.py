from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=32)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Company {self.name} (id={self.pk})'


class Specialty(models.Model):
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    picture = models.URLField(default='https://place-hold.it/100x60')

    def __str__(self):
        return f'Specialty {self.code} (id={self.pk})'


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ManyToManyField(Specialty, related_name='vacancies')
    company = models.ManyToManyField(Company, related_name='companies')
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()
    skills = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'Vacancy {self.title} (id={self.pk})'


class Application(models.Model):
    written_username = models.CharField(max_length=64)
    written_phone = models.CharField(max_length=32)
    written_cover_letter = models.TextField()
    vacancy = models.ManyToManyField(Vacancy, related_name='applications')
    user = models.ManyToManyField(User, related_name="applications", null=True)
