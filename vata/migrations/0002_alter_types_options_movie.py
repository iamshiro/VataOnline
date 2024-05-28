# Generated by Django 5.0.6 on 2024-05-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='types',
            options={'verbose_name': 'Тип контента', 'verbose_name_plural': 'Типы контента'},
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='Постер')),
                ('year', models.PositiveSmallIntegerField(default=2024, verbose_name='Дата выхода')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('url', models.URLField()),
                ('genres', models.ManyToManyField(to='vata.genre', verbose_name='Жанры')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
    ]