from django.contrib import admin
from .models import Warehouse, Order


admin.site.register(Order)
admin.site.register(Warehouse)