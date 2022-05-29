from django.contrib import admin

from .models import Category,Product,Tenant,Building
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Building)
admin.site.register(Tenant)