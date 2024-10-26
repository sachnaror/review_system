# reviews/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Point root to the home view
    path('business/<int:id>/', views.business_qr_view, name='business_qr'),
    path('reviews/<int:id>/rate', views.review_stars, name='review_stars'),
    path('feedback/', views.feedback, name='feedback'),
]
