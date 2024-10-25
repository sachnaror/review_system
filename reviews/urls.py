from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),         # Main page with rating
    path('thank_you/', views.thank_you, name='thank_you'),  # High rating page
    path('feedback/', views.feedback, name='feedback'),     # Low rating page
]
