from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Product._meta.fields]