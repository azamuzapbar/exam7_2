from django.db import models
from django.db.models import TextChoices

class StatusChoices(TextChoices):
    ACTIVE = 'Active', 'Активна'
    NOT_ACTIVE = 'NOT_ACTIVE', 'Неактивна'


class Article(models.Model):
    status = models.CharField(verbose_name='Статус', choices=StatusChoices.choices, max_length=100,
                              default=StatusChoices.ACTIVE)
    email = models.EmailField(verbose_name='Почта', max_length=200, null=True, blank=False)
    text = models.TextField(verbose_name='Текст', max_length=3000, null=False, blank=False)
    author = models.TextField(verbose_name='Автор', max_length=3000, null=False, blank=False, default='')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.email}-{self.author}-{self.text}'

    def get_absolute_url(self):
        return f'/news/{self.id}'