import datetime
from django.db import models
from django.core.exceptions import ValidationError
from common.models import Media

from django_ckeditor_5.fields import CKEditor5Field

from products.models import Product


class Vacancy(models.Model):
    title = models.CharField("Наименование", max_length=120)
    image = models.ForeignKey(Media, on_delete=models.SET_NULL,
                              null=True, blank=True)
    responsibilities = CKEditor5Field("Обязанности")
    requirements = CKEditor5Field("Требования")
    conditions = CKEditor5Field("Условия")

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.title


class Action(models.Model):
    title = models.CharField("Наименование", max_length=120)
    special_offer = models.BooleanField("Специальное предложение",
                                        default=False)
    short_description = models.TextField("Короткое описание")
    expires_in = models.DateField("Дата окончания", blank=False)
    percentage = models.PositiveSmallIntegerField("Процент скидки")
    in_discount = models.BooleanField("Скидка", default=False)

    tags = models.ManyToManyField("ActionTag",
                                  verbose_name="Тэги",
                                  blank=True)

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    def __str__(self):
        return self.title

    def clean(self):
        if self.expires_in < datetime.date.today():
            raise ValidationError("Дата окончания должна быть не меньше чем сегодня !")


class ActionTag(models.Model):
    title = models.CharField("Наименование", max_length=120)

    class Meta:
        verbose_name = "Тэг акции"
        verbose_name_plural = "Тэги акции"

    def __str__(self):
        return self.title


class ActionImage(models.Model):
    action = models.ForeignKey(Action, on_delete=models.CASCADE,
                               verbose_name="Акция",
                               related_name="action_images")
    image = models.ForeignKey(Media, on_delete=models.CASCADE,
                              verbose_name="Фото")

    class Meta:
        verbose_name = "Фото акции"
        verbose_name_plural = "Фото акции"

    def __str__(self):
        return f"Акция: {self.action}|ID: {self.id}"


class OnlineAppointment(models.Model):
    phone_number = models.CharField("Номер телефона",
                                    max_length=20)
    full_name = models.CharField("Ф.И.О",
                                 max_length=120)
    book_date = models.DateField("Дата записи")
    active = models.BooleanField("Статус",
                                 default=True)

    class Meta:
        verbose_name = "Онлайн заявка"
        verbose_name_plural = "Онлайн заявки"

    def __str__(self):
        return self.full_name

    def clean(self):
        if self.book_date < datetime.date.today():
            raise ValidationError("Дата записи должна быть больше чем вчера !")


class PhotoGalleryCategory(models.Model):
    title = models.CharField("Наименование", max_length=120)

    class Meta:
        verbose_name = "Категория фотогалереи"
        verbose_name_plural = "Категории фотогалереи"

    def __str__(self):
        return self.title


class PhotoGallery(models.Model):
    photo = models.ForeignKey(Media, on_delete=models.CASCADE,
                              verbose_name="Фото")
    category = models.ForeignKey(PhotoGalleryCategory,
                                 on_delete=models.CASCADE,
                                 verbose_name="Категория")

    class Meta:
        verbose_name = "Фотография галереи"
        verbose_name_plural = "Фотографии галереи"

    def __str__(self):
        return f"ID: {self.id}| Категория: {self.category}"


class License(models.Model):
    photo = models.ForeignKey(Media, on_delete=models.CASCADE,
                              verbose_name="Фотография")
    title = models.CharField("Наименование", max_length=120)

    class Meta:
        verbose_name = "Лицензия"
        verbose_name_plural = "Лицензии"

    def __str__(self):
        return f"License: {self.title}"


class ContactChiefDoctor(models.Model):
    phone_number = models.CharField("Номер телефона", max_length=20)
    full_name = models.CharField("Ф.И.О", max_length=120)
    message = models.TextField("Обращение")
    active = models.BooleanField("Статус", default=True)

    class Meta:
        verbose_name = "Обращение к глав. Врачу"
        verbose_name_plural = "Обращении к глав. Врачу"

    def __str__(self):
        return f"Ф.И.О: {self.full_name}|Номер телефона: {self.phone_number}"


class Specialist(models.Model):
    full_name = models.CharField("Ф.И.О", max_length=120)
    position = models.CharField("Позиция в клинике", max_length=120)
    about = CKEditor5Field("Про врача коротко")
    certificates = CKEditor5Field("Сертификаты врача")
    photo = models.ForeignKey(Media, on_delete=models.SET_NULL,
                              null=True, blank=True)
    experience_in_company = models.CharField("Опыт работы в клинике", max_length=120)
    experience_in_field = models.CharField("Опыт работы в этой области", max_length=120)
    experience_in_years = models.CharField("Опыт работы в годах", max_length=120)

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"

    def __str__(self):
        return self.full_name


class Diploma(models.Model):
    specialist = models.ForeignKey(Specialist,
                                   on_delete=models.CASCADE,
                                   related_name='diploma',
                                   verbose_name="Врач к которому принадлежит диплом !")
    file = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name="Файл диплома")

    class Meta:
        verbose_name = "Диплом"
        verbose_name_plural = "Дипломы"

    def __str__(self):
        return self.title


class NewsCategory(models.Model):
    title = models.CharField(max_length=120, verbose_name="Наименование")
    image = models.ForeignKey(Media, on_delete=models.SET_NULL,
                              verbose_name="Фото",
                              null=True, blank=True)

    class Meta:
        verbose_name = "Категория новостей"
        verbose_name_plural = "Категории новостей"

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=120, verbose_name="Наименование")
    image = models.ForeignKey(Media, on_delete=models.CASCADE,
                              verbose_name="Изображение")
    desc = CKEditor5Field("Описание")
    created_at = models.DateTimeField(verbose_name="Дата добавления", auto_now_add=True)
    special_offer = models.BooleanField("Является ли спец. предложением",
                                        default=False)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE,
                                 verbose_name="Категория")
    published = models.BooleanField(default=False, verbose_name="Показано ли на сайте")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


class Contacts(models.Model):
    address = models.CharField(max_length=120, verbose_name="Адрес")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    work_time = models.CharField(max_length=120, verbose_name="Рабочее время")

    telegram = models.URLField(verbose_name="Телеграм")
    instagram = models.URLField(verbose_name="Инстаграм")
    facebook = models.URLField(verbose_name="Фейсбук")
    vkontakte = models.URLField(verbose_name="Вконтакте")
    location = models.URLField(verbose_name="Локация")


    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.address



class StoryCategory(models.Model):
    title = models.CharField(max_length=120, verbose_name="Наименование")
    image = models.ForeignKey(Media, on_delete=models.SET_NULL,
                              null=True, blank=True,
                              verbose_name="Фото")

    class Meta:
        verbose_name = "Категория сторисов"
        verbose_name_plural = "Категории сторисов"

    def __str__(self):
        return self.title


class Story(models.Model):
    title = models.CharField(max_length=120, verbose_name="Наименование")
    file = models.ForeignKey(Media, on_delete=models.CASCADE,
                             verbose_name="Фото или гиф")
    order = models.IntegerField("Порядок")
    published = models.BooleanField(default=False, verbose_name="Показывается ли на сайте")
    category = models.ForeignKey(StoryCategory, on_delete=models.CASCADE,
                                 verbose_name="Категория сториса")

    class Meta:
        verbose_name = "Сторис"
        verbose_name_plural = "Сторисы"

    def __str__(self):
        return self.title



class Feedback(models.Model):
    phone_number = models.CharField("Номер телефона", max_length=20)
    full_name = models.CharField("Ф.И.О", max_length=120)
    text = models.TextField("Текст")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    is_view = models.BooleanField("Показывается ли на сайте", default=True)
    image = models.ForeignKey(Media, on_delete=models.SET_NULL,
                              null=True, blank=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.full_name


class StoryProduct(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE,
                              related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='stories')
