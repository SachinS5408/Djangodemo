from django.contrib import admin
from shop.models import category,Product
from django.http import HttpResponse
# Register your models here.
admin.site.register(category)
admin.site.register(Product)
# Register your models here.
