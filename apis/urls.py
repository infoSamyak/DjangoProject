from django.urls import path, include
from users import urls as users_urls
from products import urls as products_urls

urlpatterns = [
    path('users/', include(users_urls)),
    path('products/', include(products_urls)),
]
