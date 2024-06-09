from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    years_of_experience = models.PositiveIntegerField()
    education = models.TextField()
    hospital = models.CharField(max_length=100)

    def __str__(self):
        return f'Dr. {self.user.userprofile.first_name} {self.user.userprofile.last_name}'

class MedicalRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    record_type = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.record_type} - {self.user.userprofile.first_name} {self.user.userprofile.last_name}'


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f'Appointment with Dr. {self.doctor.user.userprofile.last_name} on {self.date}'

class Medication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} for {self.user.userprofile.first_name} {self.user.userprofile.last_name}'

class FitnessProgram(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.user.userprofile.first_name} {self.user.userprofile.last_name}'

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.user.userprofile.first_name} {self.user.userprofile.last_name} at {self.created_at}'
