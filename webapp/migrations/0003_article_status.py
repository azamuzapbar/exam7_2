# Generated by Django 4.1.2 on 2022-10-15 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_article_delete_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('Active', 'Активна'), ('NOT_ACTIVE', 'Неактивна')], default='Active', max_length=100, verbose_name='Статус'),
        ),
    ]
