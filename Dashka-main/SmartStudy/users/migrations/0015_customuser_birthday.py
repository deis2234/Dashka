# Generated by Django 4.2.5 on 2023-11-16 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]