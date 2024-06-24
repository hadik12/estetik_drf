from rest_framework import serializers

from products.models import *
from common.serializers import MediaURLSerializer


class ProductImageSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = ProductImage
        exclude = ['product']
        read_only_fields = ['id', 'image']


class ProductListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    price = serializers.FloatField()
    category = serializers.CharField(source='category.title')
    product_images = ProductImageSerializer(many=True)


class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        exclude = ['product']


class CharacteristicValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacteristicValue
        fields = ['id', 'title']
        read_only_fields = fields


class CharacteristicSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    values = CharacteristicValueSerializer(many=True)


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    product_images = ProductImageSerializer(many=True)
    recommended_products = serializers.SerializerMethodField()
    instructions = InstructionSerializer(many=True)
    characteristics = CharacteristicSerializer(many=True)

    class Meta:
        model = Product
        exclude = ['created_at', 'manufacturer']



class OrderItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class CreateOrderSerializer(serializers.ModelSerializer):
    products = serializers.ListField(child=OrderItemSerializer())

    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'products')


class ManufacturerListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    products_count = serializers.SerializerMethodField()

    def get_products_count(self, obj):
        return obj.product_set.count()


class CategoryListSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'title', 'products_count')
        read_only_fields = fields

    def get_products_count(self, obj):
        return obj.product_set.count()

