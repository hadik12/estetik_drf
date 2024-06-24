# Generated by Django 5.0.6 on 2024-05-20 13:51

import django.db.models.deletion
import django_ckeditor_5.fields
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinics', '0004_alter_article_desc_alter_news_desc_and_more'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Заголовок сервиса')),
                ('subtitle', models.CharField(max_length=120, verbose_name='Подзаголовок сервиса')),
                ('short_desc', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Короткое описание')),
                ('price', models.FloatField(verbose_name='Цена сервиса')),
                ('long_desc', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Подробное описание')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='Фото карточки сервиса')),
            ],
            options={
                'verbose_name': 'Сервис',
                'verbose_name_plural': 'Сервисы',
            },
        ),
        migrations.CreateModel(
            name='ProcedureCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название процедуры')),
                ('price', models.FloatField(verbose_name='Цена процедуры')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedures', to='services.service', verbose_name='Сервис к которому принадлежит эта процедура')),
            ],
            options={
                'verbose_name': 'Стоимость процедуры',
                'verbose_name_plural': 'Стоимость процедур',
            },
        ),
        migrations.CreateModel(
            name='OrderService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=120, verbose_name='Номер телефона')),
                ('full_name', models.CharField(max_length=120, verbose_name='Ф.И.О')),
                ('book_date', models.DateField(verbose_name='Дата брони')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('accepted', 'Принятый'), ('cancelled', 'Отмененный'), ('finished', 'Законченный')], default='new', max_length=20, verbose_name='Статус брони')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service', verbose_name='Сервис')),
            ],
            options={
                'verbose_name': 'Бронь услуги',
                'verbose_name_plural': 'Брони услуг',
            },
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, verbose_name='Значение')),
                ('duration', models.IntegerField(verbose_name='Длительность')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characteristics', to='services.service', verbose_name='Сервис к которому принадлежит характеристика')),
            ],
            options={
                'verbose_name': 'Характеристика сервиса',
                'verbose_name_plural': 'Характеристики сервисов',
            },
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование категории сервисов')),
                ('order', models.IntegerField(default=0, verbose_name='Порядок категории')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='Фото категории')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='services.servicecategory')),
            ],
            options={
                'verbose_name': 'Категория сервиса',
                'verbose_name_plural': 'Категории сервисов',
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='services.servicecategory', verbose_name='Категория сервиса'),
        ),
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='Фото сервиса')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='services.service', verbose_name='Сервис к которому принадлежит фото')),
            ],
            options={
                'verbose_name': 'Фото сервиса',
                'verbose_name_plural': 'Фото сервисов',
            },
        ),
        migrations.CreateModel(
            name='WhoPerformsService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_specialists', to='services.service', verbose_name='Сервис который специалист предоставляет')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialist_services', to='clinics.specialist', verbose_name='Специалист который предоставляет сервис')),
            ],
            options={
                'verbose_name': 'Кто проводит процедуру',
                'verbose_name_plural': 'Кто проводит процедуры',
            },
        ),
    ]
