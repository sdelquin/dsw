from django.urls import path

from . import views

urlpatterns = [
    path('incoming/', views.incoming_transfer, name='incoming_transfer'),
]
