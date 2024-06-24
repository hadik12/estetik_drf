from django.contrib import admin

from services.models import *
from mptt.admin import DraggableMPTTAdmin


@admin.register(ServiceCategory)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'title', 'order')
    list_display_links = ('title',)


class ServiceImageTabularInline(admin.TabularInline):
    model = ServiceImage
    fk_name = "service"
    extra = 5


class CharacteristicTabularInline(admin.TabularInline):
    model = Characteristic
    fk_name = "service"
    extra = 4


class ProcedureTabularInline(admin.TabularInline):
    model = ProcedureCost
    fk_name = "service"
    extra = 5


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'subtitle')
    list_display_links = ('title',)
    list_filter = ('category',)
    search_fields = ('title', 'subtitle')
    inlines = [ServiceImageTabularInline,
               CharacteristicTabularInline,
               ProcedureTabularInline]


@admin.register(ServiceImage)
class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'service')


@admin.register(Characteristic)
class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'duration')
    list_display_links = ('value',)


@admin.register(ProcedureCost)
class ProcedureCostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'service')
    list_display_links = ('title',)


@admin.register(WhoPerformsService)
class WhoPerformsServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'specialist', 'service']


@admin.register(OrderService)
class OrderServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'book_date', 'service', 'status')
