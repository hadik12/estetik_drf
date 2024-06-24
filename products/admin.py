from mptt.admin import DraggableMPTTAdmin
from django.contrib import admin
from products.models import *


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'title', 'created_at', 'parent')
    list_display_links = ('title',)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at', 'category', 'manufacturer',
                    'discount')


class CharacteristicValueTabularInline(admin.TabularInline):
    model = CharacteristicValue
    fk_name = 'characteristic'
    extra = 2


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('title', 'product')
    inlines = [CharacteristicValueTabularInline]


@admin.register(Instruction)
class InstructionAdmin(admin.ModelAdmin):
    list_display = ('instruction', 'product')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'image']


