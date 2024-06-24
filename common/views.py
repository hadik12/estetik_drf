from rest_framework.generics import RetrieveAPIView

from common.models import CommonSettings
from common.serializers import CommonSettingsSerializer


class CommonSettingsAPIView(RetrieveAPIView):
    queryset = CommonSettings.objects.all()
    serializer_class = CommonSettingsSerializer

    def get_object(self):
        return CommonSettings.objects.first()



