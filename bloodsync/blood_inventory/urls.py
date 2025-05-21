# blood_inventory/urls.py
from django.urls import path
from .views import (
    admin_dashboard, 
    admin_donor_records, 
    barangay_dashboard, 
    add_donor, 
    add_blood_stock
)

urlpatterns = [
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin-donor-records/', admin_donor_records, name='admin_donor_records'),
    path('barangay-dashboard/', barangay_dashboard, name='barangay_dashboard'),
    path('add-donor/', add_donor, name='add_donor'),
    path('add-blood-stock/', add_blood_stock, name='add_blood_stock'),
]