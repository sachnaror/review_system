# reviews/views.py
from django.shortcuts import get_object_or_404, redirect, render

from .models import Business
from .utils import \
    generate_qr_code  # Ensure generate_qr_code is properly imported


def home(request):
    businesses = []  # Replace with your actual data
    print('Rendering home with businesses:', businesses)  # Print to console
    return render(request, 'reviews/home.html', {'businesses': businesses})

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

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print((BASE_DIR / 'reviews/templates/reviews/home.html').exists())
