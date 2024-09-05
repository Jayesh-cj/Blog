from django.contrib import admin

from blogs.models import Blog, Category

# Register your models here.

admin.site.register(Category)

# Customizinfg admin panel to view other details with blog table
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'user', 'created_at']

