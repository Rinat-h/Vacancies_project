from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from django import forms

from vacancies.models import Company, Vacancy, Specialty


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'location', 'logo', 'employee_count', 'description')
        labels = {'name': 'Название компании', 'location': 'География', 'logo': 'Логотип',
                  'employee_count': 'Количество человек в компании', 'description': 'Информация о компании'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit(name='Save', value='Сохранить'))
        self.helper.form_method = 'post'


class VacancyForm(forms.ModelForm):

    specialty = forms.SpecialtyChoiceField(queryset=Specialty.objects.all(), empty_label='Выберите специализацию')

    class Meta:
        model = Vacancy
        fields = ('title', 'specialty', 'salary_min', 'salary_max', 'skills', 'description')

        labels = {'title': 'Название вакансии', 'salary_min': 'Зарплата от',
                  'salary_max': 'Зарплата до', 'skills': 'Требуемые навыки', 'description': 'Описание вакансии'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('title'),
                Column('specialty')
            ),
            Row(
                Column('salary_min'),
                Column('salary_max')
            ),
            'skills',
            'description',
            Submit(name='Save', value='Сохранить')
        )
        self.fields['skills'].widget = forms.Textarea(attrs={'rows': 2, 'cols': 25})
