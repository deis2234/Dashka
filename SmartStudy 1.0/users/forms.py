
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser, Group
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import Lesson

class CustomUserCreationForm(UserCreationForm):
    gender = forms.ChoiceField(choices=CustomUser.GENDER_CHOICES, label='Пол', required=True)
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES, label='Тип пользователя', required=True)
    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='RU'),label='Номер телефона', required=False)
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Дата рождения', required=False)

    class Meta:
        model = CustomUser
        fields = ('surname', 'name', 'middlename', 'phone_number','gender', 'user_type','birthday')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('surname', 'name', 'middlename', 'gender', 'birthday', 'groups')

class CustomUserEditForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = CustomUser
        fields = ['surname', 'name', 'middlename', 'birthday', 'groups', 'user_type']


class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)  # Handle password separately
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'password', 'surname', 'name', 'middlename',
            'phone_number', 'is_account_confirmed', 'gender', 'user_type',
            'birthday', 'groups'
        ]
        widgets = {
            'groups': forms.CheckboxSelectMultiple,
        }


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['subject', 'location', 'time', 'link', 'day']

    # Можете добавить дополнительные настройки для полей, если необходимо
    widgets = {
        'time': forms.TimeInput(attrs={'type': 'time'}),}