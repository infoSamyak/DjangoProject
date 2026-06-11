from django.urls import path
from .views import products

urlpatterns = [
    path("", products),
    path("<int:id>", products),
]
