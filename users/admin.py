from django.contrib import admin
from .models import Users


@admin.register(Users)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "fname")
    search_fields = ("fname",)
