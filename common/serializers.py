from rest_framework import serializers

from common.models import *


# TODO: Для того чтобы получить объект на основе класса MEDIA
# объект на основе класса MEDIA ---> Media file

class MediaURLSerializer(serializers.Serializer):
    def to_representation(self, media):
        if not media:
            return None
        try:
            # Универсальный url для медиа файлов
            # only_medias/first.jpg
            # "http://localhost:8000/media/only_medias/first.jpg"
            return self.context["request"].build_absolute_uri(media.file.url)
        except:
            return "http://testserver" + str(media.file.url)


class CommonSettingsSerializer(serializers.ModelSerializer):
    main_gif = MediaURLSerializer()
    main_right_gif = MediaURLSerializer()
    main_left_gif = MediaURLSerializer()
    our_clinic_gif = MediaURLSerializer()
    service_page_image = MediaURLSerializer()
    specialists_page_left_image = MediaURLSerializer()
    specialists_page_right_image = MediaURLSerializer()
    actions_page_left_image = MediaURLSerializer()
    actions_page_right_image = MediaURLSerializer()
    products_page_image = MediaURLSerializer()
    contacts_page_image = MediaURLSerializer()
    vacancy_page_image = MediaURLSerializer()
    product_page_left_image = MediaURLSerializer()
    product_page_right_image = MediaURLSerializer()

    class Meta:
        model = CommonSettings
        fields = "__all__"

