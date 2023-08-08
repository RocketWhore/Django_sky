
from django.contrib import admin

from materials.models import Materials

# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('pk','title', 'preview', 'body', )
