# reviews/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('business/<int:id>/', views.business_qr_view, name='business_qr'),
    path('review/<int:id>/', views.review_stars, name='review_stars'),
    path('feedback/', views.feedback, name='feedback'),
]
