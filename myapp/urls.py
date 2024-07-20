from django.urls import path
from .views import api_protected

urlpatterns = [
    path('api/protected/', api_protected, name='api_protected'),
]