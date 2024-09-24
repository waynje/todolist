from datetime import date

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='usercomments',
        verbose_name='Пользователь'
    )
    creation_date = models.DateField(
        'Дата создания',
        default=timezone.now
    )
    text = models.TextField(
        'Текст'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.name


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
    creation_date = models.DateField(
        'Дата создания',
        default=timezone.now
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
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='commentstask',
        verbose_name='Комментарий',
        null=True
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self) -> str:
        return f'Задача {self.name} в категории {self.category}'
