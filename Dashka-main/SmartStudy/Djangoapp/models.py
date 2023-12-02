from django.db import models


# Create your models here.
class Groups(models.Model):
    name = models.CharField(max_length=50, verbose_name='Номер группы')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Lecture(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название предмета')
    groups = models.ForeignKey(Groups, on_delete=models.CASCADE, verbose_name='Группа',null=True)
    short_dest = models.CharField(max_length=255, verbose_name='Тема лекции')
    link = models.URLField(blank=True, null=True, verbose_name='Ссылка на занятие' )
    date = models.DateTimeField('Дата Публикации', null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Лекция"
        verbose_name_plural = "Лекции"





class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent_folder = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subfolders')
    link = models.URLField(blank=True, null=True, verbose_name='Ссылка на архив')

    def __str__(self):
        return self.name