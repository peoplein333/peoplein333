from django.urls import path
from sang import views

app_name = 'sang'

urlpatterns = [
    path('', views.sang2, name='sang2'),
]
