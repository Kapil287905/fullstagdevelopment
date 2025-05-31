from django.contrib import admin
from .models import Recipe

# Register your models here.
@admin.register(Recipe)
class RecipeAfmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Recipe._meta.fields]