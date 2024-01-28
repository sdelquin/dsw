from django.urls import path, register_converter

from . import converters, views

app_name = 'events'

register_converter(converters.EventConverter, 'event')

urlpatterns = [
    path('', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('<event:event>/', views.detail, name='detail'),
]
