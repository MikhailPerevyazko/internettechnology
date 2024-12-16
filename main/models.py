from django.db import models


# Класс создает поля в базе данных
class Task(models.Model):
    title = models.CharField('Название', max_length = 50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title
    
    # Класс меняет task/tasks  на задача/задачи
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'