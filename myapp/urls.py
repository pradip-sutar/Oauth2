from django.urls import path
from . import views

urlpatterns = [
    path('api_protected/', views.protected_view, name='api_protected'),
]