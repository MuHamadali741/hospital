from rest_framework import viewsets
from .models import *
from .serializers import *


class UserProfileViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers


class DoctorViewSets(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers


class MedicalRecordViewSets(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializers


class AppointmentViewSets(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers


class MedicationViewSets(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializers


class FitnessProgramViewSets(viewsets.ModelViewSet):
    queryset = FitnessProgram.objects.all()
    serializer_class = FitnessProgramSerializers


class NotificationViewSets(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializers





