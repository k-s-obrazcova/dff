# Generated by Django 5.0 on 2023-12-14 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_publishing_house_agent_patronymic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название характеристики')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название компании')),
                ('agent_firstname', models.CharField(max_length=255, verbose_name='Фамилия представителя')),
                ('agent_name', models.CharField(max_length=255, verbose_name='Имя представителя')),
                ('agent_patronymic', models.CharField(max_length=255, null=True, verbose_name='Отчество представителя ')),
                ('agent_telephone', models.CharField(max_length=255, null=True, verbose_name='Телефон представителя')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес поставщика')),
                ('logical_del', models.BooleanField(default=True, verbose_name='Логическое удаление')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=20, verbose_name='Номер поставки')),
                ('date_supply', models.DateTimeField(verbose_name='Дата поставки')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library.supplier', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Поставка',
                'verbose_name_plural': 'Поставки',
            },
        ),
    ]
