from django.urls import path

from common.views import CommonSettingsAPIView
urlpatterns = [
    path("common_settings/", CommonSettingsAPIView.as_view(), name="common_settings")
]