from django.contrib.auth.models import User
from django.db import models
from model_utils import Choices
from vacancies_project.settings import MEDIA_SPECIALITY_IMAGE_DIR, MEDIA_COMPANY_IMAGE_DIR


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=32)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR)
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'Company {self.name} (id={self.pk})'


class Specialty(models.Model):
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR)

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
    user = models.ManyToManyField(User, related_name="applications", null=False)


class Resume(models.Model):
    Status = Choices('Не ищу работу', 'Рассматриваю предложения', 'Ищу работу')
    Grade = Choices('Стажер', 'Джуниор', 'Миддл', 'Синьор', 'Лид')

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    status = models.CharField(choices=Status, max_length=32)
    salary = models.IntegerField()
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    grade = models.CharField(choices=Grade, max_length=16)
    education = models.TextField()
    experience = models.TextField()
    portfolio = models.CharField(max_length=64)
