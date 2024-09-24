from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        'Название',
        max_length=56,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(
        'Название',
        max_length=56,
    )
    description = models.CharField(
        'Описание',
        max_length=256
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='categorytasks',
        verbose_name='Категория',
    )
    execution_date = models.DateField(
        'Дата исполнения'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='usertasks',
        verbose_name='Пользователь'
    )
    complete = models.BooleanField(
        'Выполнено',
        default=False,
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self) -> str:
        return f'Задача {self.name} в категории {self.category}'