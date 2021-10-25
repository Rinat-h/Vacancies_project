from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from django import forms

from vacancies.models import Company, Vacancy, Specialty, Application, Resume


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'location', 'logo', 'employee_count', 'description')
        labels = {
            'name': 'Название компании',
            'location': 'География',
            'logo': 'Логотип',
            'employee_count': 'Количество человек в компании',
            'description': 'Информация о компании',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column('logo'),
            ),
            Row(
                Column('employee_count'),
                Column('location'),
            ),
            'description',
            Submit(name='Save', value='Сохранить'),
        )


class NameChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.title


class VacancyForm(forms.ModelForm):

    specialty = NameChoiceField(queryset=Specialty.objects.all(), empty_label='Выберите специализацию')

    class Meta:
        model = Vacancy
        fields = ('title', 'specialty', 'salary_min', 'salary_max', 'skills', 'description')

        labels = {
            'title': 'Название вакансии',
            'salary_min': 'Зарплата от',
            'salary_max': 'Зарплата до',
            'skills': 'Требуемые навыки',
            'description': 'Описание вакансии',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('title'),
                Column('specialty'),
            ),
            Row(
                Column('salary_min'),
                Column('salary_max'),
            ),
            'skills',
            'description',
            Submit(name='Save', value='Сохранить'),
        )
        self.fields['skills'].widget = forms.Textarea(attrs={'rows': 2, 'cols': 25})


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('written_username', 'written_phone', 'written_cover_letter')
        labels = {
            'written_username': 'Вас зовут',
            'written_phone': 'Ваш телефон',
            'written_cover_letter': 'Сопроводительное письмо',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'written_username',
            'written_phone',
            'written_cover_letter',
            Submit(name='Save', value='Отправить'),
        )


class ResumeForm(forms.ModelForm):

    specialty = NameChoiceField(queryset=Specialty.objects.all(), empty_label='Выберите специализацию')

    class Meta:
        model = Resume
        fields = ('name', 'surname', 'status', 'salary', 'specialty', 'grade', 'education', 'experience', 'portfolio')
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'status': 'Готовность к работе',
            'salary': 'Ожидаемое вознаграждение',
            'specialty': 'Специализация',
            'grade': 'Квалификация',
            'education': 'Образование',
            'experience': 'Опыт работы',
            'portfolio': 'Ссылка на портфолио',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column('surname'),
            ),
            Row(
                Column('status'),
                Column('salary'),
            ),
            Row(
                Column('specialty'),
                Column('grade'),
            ),
            'education',
            'experience',
            'portfolio',
            Submit(name='Save', value='Сохранить'),
        )
        self.fields['education'].widget = forms.Textarea(attrs={'rows': 4, 'cols': 25})
        self.fields['experience'].widget = forms.Textarea(attrs={'rows': 4, 'cols': 25})


class VacancySearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False,
                            widget=forms.TextInput(attrs={'placeholder': 'Найти работу или стажировку'}), label='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.layout = Layout(
            Row(
                Column('query'),
                Column(Submit(name='Search', value='Найти')),
            ),
        )
