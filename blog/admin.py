from django.contrib import admin

# Register your models here.
from .models import Category, Posts

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at', 'active')

admin.site.register(Category)
admin.site.register(Posts, PostsAdmin)

