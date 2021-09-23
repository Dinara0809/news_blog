from .models import News
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import re

class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.TextInput(attrs={'class': 'form-control'}))


class UserLogin(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 155 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвердить пороль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

class NewForm(forms.ModelForm):
    midel = News
    fields = ['title', 'content', 'is_public', 'category']
    widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

def clean_title(self):
    title = self.clean_data['title']
    if re.match(r'/d', title):
        raise ValidationError('Название не должно начинаться с цифры')
    return title