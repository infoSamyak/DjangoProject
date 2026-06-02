from django.urls import path, include
from users import urls

urlpatterns = [
    path('users', include(urls)),
]
