from django.urls import path

from . import views

app_name = 'transfer'

urlpatterns = [
    path('incoming/', views.incoming_transfer, name='incoming_transfer'),
]
