from django.urls import path, include
from .views import *

urlpatterns = [

    path("accounts/", include("allauth.urls")),


    path('userprofile/', UserProfileViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='userprofile_list'),
    path('userprofile/<int:pk>/', UserProfileViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='userprofile_detail'),


    path('doctor/', DoctorViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='doctor_list'),
    path('doctor/<int:pk>/', DoctorViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='doctor_detail'),


    path('medicialrecord/', MedicalRecordViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='medicialrecord_list'),
    path('medicialrecord/<int:pk>/', MedicalRecordViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name= 'medicialrecord_detail'),


    path('appointment/', AppointmentViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='appointment_list'),
    path('appointment/<int:pk>/', AppointmentViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='appointment_detail'),

    path('medication/', MedicationViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='medication_list'),
    path('medication/<int:pk>/', MedicationViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='medication_detail'),

    path('fitnessprogram/', FitnessProgramViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='fitnessprogram_list'),
    path('fitnessprogram/<int:pk>/', FitnessProgramViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='fitnessprogram_detail'),

    path('notification/', NotificationViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='notification'),
    path('notification/<int:pk>/', NotificationViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='notification'),
]
