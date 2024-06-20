# Generated by Django 5.0 on 2023-12-07 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название книги')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание книги')),
                ('count_pages', models.IntegerField(null=True, verbose_name='Количество страниц')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('release_date', models.DateField(auto_now_add=True, verbose_name='Дата выпуска')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')),
                ('update_data', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления записи')),
                ('photo', models.ImageField(null=True, upload_to='image/%Y/%m/%d', verbose_name='Фотография книги')),
                ('exists', models.BooleanField(default=True, verbose_name='Издана?')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['name', '-price'],
            },
        ),
        migrations.CreateModel(
            name='Publishing_house',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('agent_firstname', models.CharField(max_length=50, verbose_name='Фамилия представителя')),
                ('agent_name', models.CharField(max_length=50, verbose_name='Имя представителя')),
                ('agent_patronymic', models.CharField(max_length=50, null=True, verbose_name='Отчество представителя')),
                ('agent_telephone', models.CharField(max_length=20, null=True, verbose_name='Телефон представителя')),
            ],
            options={
                'verbose_name': 'Издатель',
                'verbose_name_plural': 'Издатели',
            },
        ),
        migrations.CreateModel(
            name='Passport_book',
            fields=[
                ('article', models.IntegerField(verbose_name='Артикль')),
                ('features', models.CharField(max_length=255, verbose_name='Свойства книги')),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='library.books', verbose_name='Книга')),
            ],
            options={
                'verbose_name': 'Паспорт книги',
                'verbose_name_plural': 'Паспорт книг',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('books', models.ManyToManyField(to='library.books')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AddField(
            model_name='books',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='library.publishing_house', verbose_name='Издатель'),
        ),
    ]
