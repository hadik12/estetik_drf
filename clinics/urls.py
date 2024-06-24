from django.urls import path

from clinics.views import *

urlpatterns = [
    path('actions/', ActionListAPIView.as_view(), name="actions"),
    path('online_appointments/', OnlineAppointmentCreateAPIView.as_view(), name="online_appointments"),
    path('news/', NewsListAPIView.as_view(), name="news"),
    path('specialists/', SpecialistListAPIView.as_view(), name="specialists"),
    path('contact-chief-doctor/', ContactChiefDoctorCreateAPIView.as_view(), name='contact-chief-doctor'),
    path('create_feedback/', FeedbackCreateAPIView.as_view(), name='create_feedback'),
    path('feedbacks/', FeedbackListAPIView.as_view(), name='feedbacks'),

    path('licenses/', LicenseListAPIView.as_view(), name='licenses'),
    path('vacancies/', VacancyListAPIView.as_view(), name="vacancies-list"),
    path('contacts/', ContactAPIView.as_view(), name="contacts"),
    path('news-categories/', NewsCategoryListAPIView.as_view(), name="news-categories"),
    path('photo-gallery-categories/', PhotoGalleryCategoryListAPIView.as_view(), name='photogallery-categories'),
    path('photo-galleries/', PhotoGalleryListAPIView.as_view(), name='photo-galleries'),
    path('story-categories/', StoryCategoryListAPIView.as_view(), name='story-categories'),
    path('stories/', StoryCategoriesListAPIView.as_view(), name='stories')
]
