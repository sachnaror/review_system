# reviews/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Business
from .utils import generate_qr_code

def business_qr_view(request, id):
    business = get_object_or_404(Business, id=id)
    if not business.qr_code:
        generate_qr_code(business)
    return render(request, 'business_qr.html', {'business': business})

def review_stars(request, id):
    business = get_object_or_404(Business, id=id)
    return render(request, 'review_stars.html', {'business': business})

def feedback(request):
    return render(request, 'feedback.html')
