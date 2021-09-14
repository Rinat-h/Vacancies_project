from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=32)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField(null=True)
    employee_count = models.IntegerField(null=True)

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
    salary_min = models.IntegerField(null=True)
    salary_max = models.IntegerField(null=True)
    published_at = models.DateField(null=True)
    skills = models.TextField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f'Vacancy {self.title} (id={self.pk})'
