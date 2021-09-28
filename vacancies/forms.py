from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from vacancies.models import Company


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
