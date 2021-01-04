from django.contrib import admin

# Register your models here.
from .models import Category, Posts
 
admin.site.register(Category)
admin.site.register(Posts)