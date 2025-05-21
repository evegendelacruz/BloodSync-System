# blood_inventory/forms.py
from django import forms
from .models import DonorRecord, BloodStock

class DonorRecordForm(forms.ModelForm):
    class Meta:
        model = DonorRecord
        exclude = ['added_by']
        widgets = {
            'donor_id': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'blood_type': forms.Select(attrs={'class': 'form-control'}),
            'rh_factor': forms.Select(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'barangay': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BloodStockForm(forms.ModelForm):
    class Meta:
        model = BloodStock
        fields = '__all__'
        widgets = {
            'serial_id': forms.TextInput(attrs={'class': 'form-control'}),
            'blood_type': forms.Select(attrs={'class': 'form-control'}),
            'rh_factor': forms.Select(attrs={'class': 'form-control'}),
            'volume_ml': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_of_collection': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }