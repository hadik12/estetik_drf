from django.db import models

from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


# Все медиа файлы хранить внутри одной модели
class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = 'image', "Изображение"
        VIDEO = 'video', "Видео"
        DOCUMENT = 'document', "Документ"
        GIF = 'gif', "Гиф"

    file = models.FileField(upload_to='only_medias/',
                            verbose_name="Файл",
                            validators=[FileExtensionValidator(
                                allowed_extensions=['png', 'jpg', 'svg', 'jpeg',
                                                    'mp4', 'avi', 'mkv', 'mov',
                                                    'pdf', 'doc', 'docx',
                                                    'gif']
                            )])
    file_type = models.CharField(max_length=10,
                                 verbose_name="Тип файла",
                                 choices=FileType.choices)

    class Meta:
        verbose_name = "Медиа файл"
        verbose_name_plural = "Медиа файлы"

    def __str__(self):
        return f"Id: {self.id}| Name: {self.file.name.split('/')[-1]}"

    # Метод будет срабатывать именно при загрузке объектов на основе модели
    def clean(self):
        if self.file_type not in self.FileType.values:
            raise ValidationError("Не допустимый тип файл !")
        elif self.file_type == self.FileType.IMAGE:
            if self.file.name.split(".")[-1] not in ['png', 'jpg', 'svg', 'jpeg']:
                raise ValidationError("Не допустимое изображение !")
        elif self.file_type == self.FileType.VIDEO:
            if self.file.name.split(".")[-1] not in ['mp4', 'avi', 'mkv', 'mov']:
                raise ValidationError("Не допустимое видео !")
        elif self.file_type == self.FileType.DOCUMENT:
            if self.file.name.split(".")[-1] not in ['pdf', 'doc', 'docx']:
                raise ValidationError("Не допустимый документ !")
        elif self.file_type == self.FileType.GIF:
            if self.file.name.split(".")[-1] not in ['gif']:
                raise ValidationError("Не допустимый гиф !")


class CommonSettings(models.Model):
    main_phone_number = models.CharField(max_length=20, verbose_name="Номер телефона клиники")

    main_gif = models.ForeignKey(to=Media,
                                 on_delete=models.CASCADE,
                                 verbose_name="Гиф на главной странице в header !",
                                 related_name="main_page_header_gif")

    main_text = models.TextField(verbose_name="Текст на главной странице в header !")

    main_right_gif = models.ForeignKey(to=Media,
                                       on_delete=models.CASCADE,
                                       verbose_name="Гиф на главной странице ниже акции с права !",
                                       related_name="main_page_right_gif")

    main_left_gif = models.ForeignKey(to=Media,
                                      on_delete=models.CASCADE,
                                      verbose_name="Гиф на главной странице ниже акции с лева !",
                                      related_name="main_page_left_gif")

    main_page_text_on_right_gif = models.TextField(verbose_name="Текст на гиф с права на главной странице !")

    our_clinic_gif = models.ForeignKey(to=Media,
                                       on_delete=models.CASCADE,
                                       verbose_name="Гиф на странице о клинике в header !",
                                       related_name="our_clinic_gif")

    our_clinic_text = models.TextField(verbose_name="Текст на странице о клинике !")

    service_page_image = models.ForeignKey(to=Media,
                                           on_delete=models.CASCADE,
                                           verbose_name="Фото на странице сервисы !",
                                           related_name="service_page_image")

    specialists_page_left_image = models.ForeignKey(to=Media,
                                                    on_delete=models.CASCADE,
                                                    verbose_name="Фото с лева на странице специалисты !",
                                                    related_name="specialists_page_left_image")
    specialists_page_right_image = models.ForeignKey(to=Media,
                                                     on_delete=models.CASCADE,
                                                     verbose_name="Фото с права на странице специалисты !",
                                                     related_name="specialists_page_right_image")

    specialists_page_text_on_right_photo = models.TextField(verbose_name="Текст на странице специалисты на правом фото !")

    actions_page_left_image = models.ForeignKey(to=Media,
                                                on_delete=models.CASCADE,
                                                verbose_name="Фото с лева на странице акции !",
                                                related_name="actions_page_left_image")
    actions_page_right_image = models.ForeignKey(to=Media,
                                                 on_delete=models.CASCADE,
                                                 verbose_name="Фото с права на странице акции !",
                                                 related_name="actions_page_right_image")

    actions_page_text_on_right_photo = models.TextField(verbose_name="Текст на странице специалисты на правом фото !")

    products_page_image = models.ForeignKey(to=Media,
                                            on_delete=models.CASCADE,
                                            verbose_name="Фото на странице продукты !",
                                            related_name="products_page_image")

    contacts_page_image = models.ForeignKey(to=Media,
                                            on_delete=models.CASCADE,
                                            verbose_name="Фото на странице контакты !",
                                            related_name="contacts_page_image")

    vacancy_page_image = models.ForeignKey(to=Media,
                                           on_delete=models.CASCADE,
                                           verbose_name="Фото на странице продукты !",
                                           related_name="vacancy_page_image")

    product_page_left_image = models.ForeignKey(to=Media,
                                                on_delete=models.CASCADE,
                                                verbose_name="Фото с лева на странице продукта !",
                                                related_name="product_page_left_image")

    product_page_right_image = models.ForeignKey(to=Media,
                                                 on_delete=models.CASCADE,
                                                 verbose_name="Фото с права на странице продукта !",
                                                 related_name="product_page_right_image")
    product_page_text_on_right_photo = models.TextField(verbose_name="Текст на странице продукта на правом фото !")

    class Meta:
        verbose_name = "Общие настройки"
        verbose_name_plural = "Общие настройки"

    def __str__(self):
        return f"{self.id}| {self.main_phone_number}"
