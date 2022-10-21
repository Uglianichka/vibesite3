from django.db import models
from django.utils.safestring import mark_safe

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    text = models.TextField('Текст')
    image = models.FileField('Изображение')


    def __str__(self):
        return self.title



class Meta:
    verbose_name="Задача"
    verbose_name_plural="Задачи"