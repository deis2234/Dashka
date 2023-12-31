# Generated by Django 4.2.5 on 2023-11-15 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_customuser_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='status',
            new_name='is_account_confirmed',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='fullname',
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Мужской'), ('F', 'Женский')], max_length=1, null=True, verbose_name='Пол'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(blank=True, choices=[('S', 'Студент'), ('T', 'Преподаватель')], max_length=1, null=True, verbose_name='Тип пользователя'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Адрес электронной почты'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='Номер телефона'),
        ),
    ]
