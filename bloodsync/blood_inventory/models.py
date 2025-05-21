# blood_inventory/models.py
from django.db import models
from accounts.models import User

class BloodStock(models.Model):
    BLOOD_TYPE_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    )
    RH_FACTOR_CHOICES = (
        ('+', 'Positive'),
        ('-', 'Negative'),
    )
    STATUS_CHOICES = (
        ('stored', 'Stored'),
        ('released', 'Released'),
    )
    
    serial_id = models.CharField(max_length=20, unique=True)
    blood_type = models.CharField(max_length=2, choices=BLOOD_TYPE_CHOICES)
    rh_factor = models.CharField(max_length=1, choices=RH_FACTOR_CHOICES, blank=True, null=True)
    volume_ml = models.IntegerField()
    date_of_collection = models.DateField()
    expiration_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='stored')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.serial_id

class DonorRecord(models.Model):
    BLOOD_TYPE_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    )
    RH_FACTOR_CHOICES = (
        ('+', 'Positive'),
        ('-', 'Negative'),
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    
    donor_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birthdate = models.DateField()
    age = models.IntegerField()
    blood_type = models.CharField(max_length=2, choices=BLOOD_TYPE_CHOICES)
    rh_factor = models.CharField(max_length=1, choices=RH_FACTOR_CHOICES, blank=True, null=True)
    contact_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    barangay = models.CharField(max_length=100)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"