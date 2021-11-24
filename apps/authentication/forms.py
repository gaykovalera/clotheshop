from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from django.db.models import Q

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль')

    class Meta:
        model = User
        fields = ['username', 'email', 'avatar']
        labels = {'username': 'Имя пользователя:',
                  'email': 'email'}

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise ValidationError(
                'Пароли должны совпадать'
            )
        return self.cleaned_data['password2']

    def clean(self):
        user = User.objects.filter(
            Q(username=self.cleaned_data['username'])
            | Q(email=self.cleaned_data['email'])
        ).first()
        if user:
            raise ValidationError('Пользователь с такими данными уже существует')
        return super().clean()


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def clean(self):
        user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        if not user:
            raise ValidationError('Введённые данные неверны')
        return self.cleaned_data


