from django.contrib import admin
from category.models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('categoryName',)}
    list_display=('categoryName','slug')

admin.site.register(Category,CategoryAdmin)