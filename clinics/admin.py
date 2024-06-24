from django.contrib import admin

from clinics.models import *


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title', 'requirements', 'responsibilities', 'conditions']


class ActionImageTabularInline(admin.TabularInline):
    fk_name = 'action'
    model = ActionImage
    extra = 3


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'expires_in', 'percentage', 'in_discount']
    search_fields = ['title', 'short_desc', 'desc']
    list_filter = ['in_discount', 'special_offer', 'expires_in']
    list_display_links = ['title']
    inlines = [ActionImageTabularInline]


@admin.register(ActionTag)
class ActionTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


@admin.register(ActionImage)
class ActionImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']


@admin.register(OnlineAppointment)
class OnlineAppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number', 'book_date', 'active']
    search_fields = ['phone_number', 'full_name']
    list_filter = ['active']
    list_editable = ['active']


@admin.register(PhotoGalleryCategory)
class PhotoGalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo']


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


@admin.register(ContactChiefDoctor)
class ContactChiefDoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number', 'active']
    list_editable = ['active']


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'position']
    list_filter = ['position']


@admin.register(Diploma)
class DiplomaAdmin(admin.ModelAdmin):
    list_display = ['id', 'specialist', 'file']


# Зерегистрировать категории новостей
@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image']
    search_fields = ['title']


# Сами новости
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_at', 'published']
    search_fields = ['title', 'desc']
    list_filter = ['published', 'category', 'special_offer']


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'address', 'work_time']
    search_fields = ['phone_number', 'address']


@admin.register(StoryCategory)
class StoryCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'published', 'order']
    search_fields = ['title', 'desc']
    list_filter = ['published', 'category']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'created_at', 'phone_number', 'is_view']
    list_filter = ['is_view']
    search_fields = ['full_name', 'phone_number', 'text']
