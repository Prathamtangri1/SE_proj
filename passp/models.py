from django.db import models
from django.contrib.auth.models import User

class Passport(models.Model):
    passport_number = models.CharField(max_length = 10, primary_key=True)
    name = models.CharField(max_length = 40)
    father_name = models.CharField(max_length = 100)
    dob = models.CharField(max_length = 10)
    current_add = models.CharField(max_length = 400)
    permanent_add = models.CharField(max_length = 400)
    gender = models.CharField(max_length = 6)
    phone = models.CharField(max_length = 10)
    email = models.CharField(max_length = 40)

    def __str__(self):
        return self.passport_number

class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    status = models.CharField(max_length = 10)

    def __str__(self):
        return self.user.username