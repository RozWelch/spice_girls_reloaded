from django.contrib import admin
from .models import Spices, Category


class SpicesAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Spices, SpicesAdmin)
admin.site.register(Category, CategoryAdmin)
