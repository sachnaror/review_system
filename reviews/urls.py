# reviews/urls.py
from django.urls import path

from . import views
from .views import business_detail, home

urlpatterns = [
  # Point root to the home view
    path('', home, name='home'),  # Home page
    path('business/<str:google_business_id>/', business_detail, name='business_detail'),
    path('business/<int:id>/', views.business_qr_view, name='business_qr'),
    path('reviews/<int:id>/rate', views.review_stars, name='review_stars'),
    path('feedback/', views.feedback, name='feedback'),
]

