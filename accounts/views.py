from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'accounts/register.html'


# SuccessMessageMixin не реализован
class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'
#    success_message = "Успешный вход! Перенаправляем на главную страницу"
