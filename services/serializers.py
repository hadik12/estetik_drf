from rest_framework import serializers

from services.models import *
from common.serializers import MediaURLSerializer
from clinics.serializers import SpecialistListSerializer
from clinics.models import Specialist, Diploma


class ServiceCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ('id', 'title')
        read_only_fields = fields


class ServiceListSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()
    category = serializers.CharField(source='category.title')

    class Meta:
        model = Service
        fields = ('id', 'title', 'category', 'image')


class ServiceImageSerializer(serializers.Serializer):
    image = MediaURLSerializer()


class ServiceCharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ('duration', 'value')
        read_only_fields = fields


class ProcedureCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedureCost
        fields = ('title', 'price')
        read_only_fields = fields


class WhoPerformsServiceSerializer(serializers.ModelSerializer):
    specialist = SpecialistListSerializer()

    class Meta:
        model = WhoPerformsService
        fields = ('id', 'specialist')
        read_only_fields = fields


class ServiceDetailSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()
    images = ServiceImageSerializer(many=True)
    characteristics = ServiceCharacteristicSerializer(many=True)
    procedures = ProcedureCostSerializer(many=True)
    service_specialists = WhoPerformsServiceSerializer(many=True)

    class Meta:
        model = Service
        fields = ('id', 'title', 'subtitle', 'image',
                  'short_desc', 'price', 'long_desc', 'category',
                  'images', 'characteristics', 'procedures',
                  'service_specialists')
        read_only_fields = fields


class SpecialistProceduresSerializer(serializers.ModelSerializer):
    service = ServiceListSerializer()

    class Meta:
        model = WhoPerformsService
        fields = ('id', 'service')
        read_only_fields = fields


class DiplomaSerializer(serializers.ModelSerializer):
    file = MediaURLSerializer()

    class MEta:
        model = Diploma
        fields = ('file',)


class SpecialistDetailSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()
    procedures = SpecialistProceduresSerializer(many=True)
    diplomas = DiplomaSerializer(many=True)

    class Meta:
        model = Specialist
        fields = ('id', 'full_name', 'position', 'about', 'certificates',
                  'photo', 'experience_in_company',
                  'experience_in_field', 'experience_in_years',
                  'procedures', 'diplomas')
        read_only_fields = fields


class OrderServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderService
        fields = ('phone', 'full_name', 'book_date', 'service')