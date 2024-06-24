from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from django_ckeditor_5.fields import CKEditor5Field

from common.models import Media


class Category(MPTTModel):
    title = models.CharField(max_length=120, verbose_name='Наименование категории')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            verbose_name="Родитель категории",
                            null=True, blank=True,
                            related_name='children')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Manufacturer(models.Model):
    title = models.CharField(max_length=120, verbose_name='Наименование производителя')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория продукта')
    title = models.CharField(max_length=120, verbose_name="Наименование продукта")
    price = models.FloatField(verbose_name="Цена")
    created_at = models.DateTimeField(verbose_name="Дата создания",
                                      auto_now_add=True)
    top_desc = CKEditor5Field(verbose_name="Верхнее описание")
    discount = models.FloatField(verbose_name="Цена без скидки",
                                 null=True, blank=True)
    down_desc = CKEditor5Field(verbose_name="Нижнее описание")
    manufacturer = models.ForeignKey(Manufacturer,
                                     on_delete=models.CASCADE,
                                     verbose_name="Производитель продукта",
                                     related_name="manufacturer_products")


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.ForeignKey(Media,
                              on_delete=models.CASCADE,
                              null=True, blank=True,
                              verbose_name="Изображение продукта")

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name="К какому продукту принадлежит изображение",
                                related_name='product_images')

    class Meta:
        verbose_name = "Изображение продукта"
        verbose_name_plural = "Изображении продуктов"

    def __str__(self):
        return f"Id: {self.id}| Product: {self.product.title}"


class Characteristic(models.Model):
    title = models.CharField(max_length=120,
                             verbose_name="Название характеристики")
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name="К какому продукту принадлежит характеристика",
                                related_name='characteristics')

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"

    def __str__(self):
        return self.title


class CharacteristicValue(models.Model):
    title = models.CharField(max_length=120,
                             verbose_name="Название значения")

    characteristic = models.ForeignKey(Characteristic,
                                       on_delete=models.CASCADE,
                                       verbose_name="К какой характеристике принадлежит значение",
                                       related_name='values')

    class Meta:
        verbose_name = 'Значение'
        verbose_name_plural = 'Значении'

    def __str__(self):
        return self.title

class Instruction(models.Model):
    instruction = models.TextField(verbose_name="Инструкция")

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name="К какому продукту принадлежит инструкция",
                                related_name='instructions')

    class Meta:
        verbose_name = 'Инструкция'
        verbose_name_plural = 'Инструкции'

    def __str__(self):
        return self.title


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        NEW = 'new', "Новый"
        ACCEPTED = 'accepted', "Принятый"
        PROGRESS = 'progress', "В прогрессе"
        CANCELLED = 'cancelled', "Отмененный"
        FINISHED = 'finished', "Законченный"


    full_name = models.CharField(max_length=120, verbose_name="Ф.И.О")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    status = models.CharField(verbose_name="Статус заказа",
                              max_length=20,
                              choices=OrderStatus.choices,
                              default=OrderStatus.NEW)
    total_price = models.FloatField(verbose_name="Окончательная цена",
                                    default=0)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)


    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return self.full_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name="К какому заказу принадлежит продукт",
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Какой продукт принадлежит к заказу",
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="Число продукта",
                                   default=1)

    class Meta:
        verbose_name = "Продукт внутри заказа"
        verbose_name_plural = "Продукты внутри заказов"
        unique_together = ['order', 'product']

    def __str__(self):
        return f"Id: {self.id}| Q: {self.quantity}"

    @property
    def total_price(self):
        return self.product.price * self.quantity




