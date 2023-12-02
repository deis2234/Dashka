# models.py
import re

from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse


class Group(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название группы", unique=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = [
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    ]

    STUDENT = 'S'
    TEACHER = 'T'

    USER_TYPE_CHOICES = [
        (STUDENT, 'Студент'),
        (TEACHER, 'Преподаватель'),
    ]

    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    name = models.CharField(max_length=100, verbose_name="Имя")
    middlename = models.CharField(max_length=100, verbose_name="Отчество", null=True, blank=True)
    email = models.EmailField(verbose_name='Адрес электронной почты', unique=True)
    phone_number = PhoneNumberField(verbose_name="Номер телефона", null=True, blank=True)
    is_account_confirmed = models.BooleanField(default=False, verbose_name='Подтверждение аккаунта')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол', null=True, blank=True)
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, verbose_name='Тип пользователя', null=True,
                                 blank=True)
    birthday = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    groups = models.ManyToManyField(Group, verbose_name="Группы", related_name="users", blank=True)
    fullname = models.CharField(max_length=255, verbose_name="Полное имя", null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return f"{self.surname} {self.name} {self.middlename}"

    def __str__(self):
        return self.get_full_name()


class Day(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    time = models.TimeField(help_text="Format: HH:MM")
    link = models.URLField(blank=True, null=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('lesson_detail', args=[str(self.pk)])

    def get_time_lowercase(self):
        return self.time.strftime('%H:%M').lower()

    def __str__(self):
        return f"{self.subject} at {self.time.strftime('%H:%M')}"

    def get_abbreviation(self):
        words = re.split(' |-', str(self.subject))
        abbreviation = ''.join(word[0] for word in words).upper()
        return abbreviation

class WeeklySchedule(models.Model):
    week_day = models.ForeignKey(Day, on_delete=models.CASCADE)
    lessons = models.ManyToManyField('Lesson')

    def __str__(self):
        return f"Weekly Schedule for {self.week_day}"