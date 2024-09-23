from django.contrib import admin

# Register your models here.

from .models import Project, SelectedTech, Category

admin.site.register(Project)
admin.site.register(SelectedTech)
admin.site.register(Category)
