from django.urls import path
from . import views

urlpatterns = [
    path('CSV_to_DF/', views.CSV_to_DF),
    path('missingValues/', views.missingValues),
    path('avg_ages/', views.avg_ages)
]

