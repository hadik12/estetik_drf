# Создать serializer
from rest_framework import serializers
from clinics.models import *
from common.serializers import MediaURLSerializer

from products.serializers import ProductListSerializer


class ActionImageSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = ActionImage
        fields = ('id', 'image')
        read_only_fields = fields


class ActionListSerializer(serializers.ModelSerializer):
    # Сериализатор который автоматическим образом создает поля
    # под поля указанной модельки
    action_images = ActionImageSerializer(many=True)
    tags = serializers.ListSerializer(child=serializers.CharField(source='tag.title'))

    class Meta:
        model = Action
        fields = (
            'id', 'title', 'special_offer',
            'short_description', 'expires_in',
            'percentage', 'action_images', 'tags'
        )
        read_only_fields = fields


class OnlineAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineAppointment
        fields = ('phone_number', 'full_name', 'book_date')


class NewsListSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'desc',
                  'created_at', 'special_offer')
        read_only_fields = fields


class DiplomaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    file = MediaURLSerializer()


class SpecialistListSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()

    class Meta:
        model = Specialist
        fields = ('id', 'full_name', 'position', 'photo', 'experience_in_years')
        read_only_fields = fields


# Ваша задача написать serializer для создания обращений к глав врачу


class ContactChiefDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactChiefDoctor
        fields = ('phone_number', 'full_name', 'message')
        write_only_fields = fields


class FeedbackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('full_name', 'phone_number', 'text')
        write_only_fields = fields


class FeedbackListSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = Feedback
        fields = ('full_name', 'text', 'created_at', 'image')
        read_only_fields = fields


class LicenseSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()

    class Meta:
        model = License
        fields = ('id', 'title', 'photo')
        read_only_fields = fields


class VacancyListSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'image', 'responsibilities', 'requirements',
                  'conditions')
        read_only_fields = fields


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"
        read_only_fields = [fields]


class NewsCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()

    # class Meta:
    #     model = NewsCategory
    #     fields = ('id', 'title')
    #     read_only_fields = [fields]


class NewsDetailSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()
    category = serializers.CharField(source='category.title')

    class Meta:
        model = News
        fields = ('title', 'image', 'desc', 'category', 'created_at',
                  'special_offer', 'category')
        read_only_fields = fields


class PhotoGalleryCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class PhotoGallerySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    photo = MediaURLSerializer()


class StoryCategoryListSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = StoryCategory
        fields = ('id', 'title', 'image')
        read_only_fields = fields


class StoryProductsListSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()

    class Meta:
        model = StoryProduct
        fields = ('item',)


class StoryListSerializer(serializers.ModelSerializer):
    products = StoryProductsListSerializer(many=True)
    video = MediaURLSerializer()

    class Meta:
        model = Story
        fields = ('id', 'title', 'video', 'products')


class StoryCategoryDetailSerializer(serializers.ModelSerializer):
    stories = StoryListSerializer(many=True)
    image = MediaURLSerializer()

    class Meta:
        model = StoryCategory
        fields = ('id', 'title', 'image', 'stories')
