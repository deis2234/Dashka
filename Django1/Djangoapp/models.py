from django.db import models


# Create your models here.
class Groups(models.Model):
    name = models.CharField(max_length=50, verbose_name='Номер группы')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название предмета')
    groups = models.ForeignKey(Groups, on_delete=models.CASCADE, verbose_name='Группа',null=True)
    short_dest = models.CharField(max_length=255, verbose_name='Тема лекции')
    content = models.TextField(verbose_name='Контент')
    date = models.DateTimeField('Дата Публикации', null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Лекция"
        verbose_name_plural = "Лекции"
