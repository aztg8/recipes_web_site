from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Profile, Recipe


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Имя пользователя"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Ваш пароль"
    }))


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Ваше имя"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Ваша фамилия"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Имя пользователя"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Ваша почта"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Придумайте пароль"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Подтвердите пароль"
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo', 'phone_number', 'address',
                  'job', 'telegram', 'instagram')

        widgets = {
            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),
            'job': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Профессия'
            }),
            'telegram': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телеграм'
            }),
            'instagram': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Инстаграм'
            }),
        }


class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Ваше имя"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Ваша фамилия"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Имя пользователя"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Ваша почта"
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'prepTimeMinutes',
                  'cookTimeMinutes', 'servings', 'cuisine',
                  'caloriesPerServing', 'image',
                  'category', 'difficulty')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Название рецепта"
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Описание рецепта"
            }),
            'prepTimeMinutes': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Время подготовки"
            }),
            'cookTimeMinutes': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Время приготовления"
            }),
            'servings': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Порции"
            }),
            'cuisine': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Кухня"
            }),
            'caloriesPerServing': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Калории/Порция"
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': "Фотография"
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': "Категория"
            }),
            'difficulty': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': "Сложность"
            })
        }


