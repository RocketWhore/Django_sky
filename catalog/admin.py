from django.contrib import admin

from catalog.models import Product, Category, Version


# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price', 'date_of_born', )
    list_filter = ('category',)
    search_fields = ('description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_title', 'product')
    list_filter = ('product',)