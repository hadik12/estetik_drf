import datetime
from mptt.models import MPTTModel, TreeForeignKey

from django.db import models
from django.core.exceptions import ValidationError
from django_ckeditor_5.fields import CKEditor5Field

from clinics.models import Specialist
from common.models import Media


class ServiceCategory(MPTTModel):
    title = models.CharField(max_length=100,
                             verbose_name="Наименование категории сервисов")
    order = models.IntegerField(verbose_name="Порядок категории",
                                default=0)

    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            related_name="children")

    image = models.ForeignKey(Media,
                              on_delete=models.CASCADE,
                              verbose_name="Фото категории")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория сервиса"
        verbose_name_plural = "Категории сервисов"
        ordering = ['order']

    class MPTTMeta:
        order_insertion_by = ['title']


class Service(models.Model):
    title = models.CharField(max_length=120, verbose_name="Заголовок сервиса")
    subtitle = models.CharField(max_length=120, verbose_name="Подзаголовок сервиса")
    image = models.ForeignKey(Media,
                              on_delete=models.CASCADE,
                              verbose_name="Фото карточки сервиса")
    category = models.ForeignKey(ServiceCategory,
                                 on_delete=models.CASCADE,
                                 verbose_name="Категория сервиса",
                                 related_name="services")
    short_desc = CKEditor5Field(verbose_name="Короткое описание")
    price = models.FloatField(verbose_name="Цена сервиса")
    long_desc = CKEditor5Field(verbose_name="Подробное описание")

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"

    def __str__(self):
        return self.title


class ServiceImage(models.Model):
    image = models.ForeignKey(Media,
                              on_delete=models.CASCADE,
                              verbose_name="Фото сервиса")
    service = models.ForeignKey(Service,
                                on_delete=models.CASCADE,
                                verbose_name="Сервис к которому принадлежит фото",
                                related_name='images')

    class Meta:
        verbose_name = "Фото сервиса"
        verbose_name_plural = "Фото сервисов"

    def __str__(self):
        return f"Id: {self.id} - Service: {self.service.title}"


class Characteristic(models.Model):
    value = models.CharField(max_length=255, verbose_name="Значение")
    duration = models.IntegerField(verbose_name="Длительность")

    service = models.ForeignKey(Service,
                                on_delete=models.CASCADE,
                                verbose_name="Сервис к которому принадлежит характеристика",
                                related_name="characteristics")

    class Meta:
        verbose_name = "Характеристика сервиса"
        verbose_name_plural = "Характеристики сервисов"

    def __str__(self):
        return self.value



class ProcedureCost(models.Model):
    title = models.CharField(verbose_name="Название процедуры",
                             max_length=120)
    price = models.FloatField(verbose_name="Цена процедуры")
    service = models.ForeignKey(Service,
                                on_delete=models.CASCADE,
                                verbose_name="Сервис к которому принадлежит эта процедура",
                                related_name='procedures')

    class Meta:
        verbose_name = "Стоимость процедуры"
        verbose_name_plural = "Стоимость процедур"

    def __str__(self):
        return self.title



class WhoPerformsService(models.Model):
    specialist = models.ForeignKey(Specialist,
                                   on_delete=models.CASCADE,
                                   verbose_name="Специалист который предоставляет сервис",
                                   related_name='specialist_services')
    service = models.ForeignKey(Service,
                                on_delete=models.CASCADE,
                                verbose_name="Сервис который специалист предоставляет",
                                related_name='service_specialists')

    class Meta:
        verbose_name = "Кто проводит процедуру"
        verbose_name_plural = "Кто проводит процедуры"

    def __str__(self):
        return f"Id: {self.id} - Specialist: {self.specialist.full_name} - Service: {self.service.title}"


class OrderService(models.Model):
    class OrderStatus(models.TextChoices):
        NEW = 'new', "Новый"
        ACCEPTED = 'accepted', "Принятый"
        CANCELED = 'cancelled', "Отмененный"
        FINISHED = 'finished', "Законченный"

    phone = models.CharField(max_length=120, verbose_name="Номер телефона")
    full_name = models.CharField(verbose_name="Ф.И.О", max_length=120)
    book_date = models.DateField(verbose_name="Дата брони")
    service = models.ForeignKey(Service,
                                on_delete=models.CASCADE,
                                verbose_name="Сервис")
    status = models.CharField(verbose_name="Статус брони",
                              max_length=20,
                              choices=OrderStatus.choices,
                              default=OrderStatus.NEW)

    class Meta:
        verbose_name = "Бронь услуги"
        verbose_name_plural = "Брони услуг"

    def __str__(self):
        return self.full_name

    def clean(self):
        if self.book_date < datetime.date.today():
            raise ValidationError("Дата брони должна быть больше чем сегодня")