# blood_inventory/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import BloodStock, DonorRecord
from .forms import BloodStockForm, DonorRecordForm
from accounts.models import User

def is_admin(user):
    return user.role == 'admin'

def is_barangay_official(user):
    return user.role == 'barangay_official'

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    blood_stocks = BloodStock.objects.all()
    return render(request, 'blood_inventory/admin_dashboard.html', {'blood_stocks': blood_stocks})

@login_required
@user_passes_test(is_admin)
def admin_donor_records(request):
    donors = DonorRecord.objects.all()
    return render(request, 'blood_inventory/admin_donor_records.html', {'donors': donors})

@login_required
@user_passes_test(is_barangay_official)
def barangay_dashboard(request):
    donors = DonorRecord.objects.filter(barangay=request.user.barangay)
    return render(request, 'blood_inventory/barangay_dashboard.html', {'donors': donors})

@login_required
def add_donor(request):
    if request.method == 'POST':
        form = DonorRecordForm(request.POST)
        if form.is_valid():
            donor = form.save(commit=False)
            donor.added_by = request.user
            if request.user.role == 'barangay_official':
                donor.barangay = request.user.barangay
            donor.save()
            if request.user.role == 'admin':
                return redirect('admin_donor_records')
            else:
                return redirect('barangay_dashboard')
    else:
        form = DonorRecordForm()
        if request.user.role == 'barangay_official':
            form.fields['barangay'].initial = request.user.barangay
            form.fields['barangay'].widget.attrs['readonly'] = True
            
    return render(request, 'blood_inventory/add_donor.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def add_blood_stock(request):
    if request.method == 'POST':
        form = BloodStockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = BloodStockForm()
        
    return render(request, 'blood_inventory/add_blood_stock.html', {'form': form})