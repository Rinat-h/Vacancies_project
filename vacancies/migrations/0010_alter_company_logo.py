# Generated by Django 3.2.8 on 2021-10-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0009_alter_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, default='default_logo.png', upload_to='company_images'),
        ),
    ]
