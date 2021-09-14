# Generated by Django 3.2.7 on 2021-09-13 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=32)),
                ('logo', models.URLField(default='https://place-hold.it/100x60')),
                ('description', models.TextField(null=True)),
                ('employee_count', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=32)),
                ('picture', models.URLField(default='https://place-hold.it/100x60')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('salary_min', models.IntegerField(null=True)),
                ('salary_max', models.IntegerField(null=True)),
                ('published_at', models.DateField(null=True)),
                ('skills', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('company', models.ManyToManyField(related_name='companies', to='vacancies.Company')),
                ('specialty', models.ManyToManyField(related_name='vacancies', to='vacancies.Specialty')),
            ],
        ),
    ]