# Generated by Django 4.1.6 on 2024-05-16 13:15

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0003_contactchiefdoctor_contacts_storycategory_story_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='news',
            name='desc',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='about',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Про врача коротко'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='certificates',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Сертификаты врача'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='conditions',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Условия'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='requirements',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Требования'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='responsibilities',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Обязанности'),
        ),
    ]
