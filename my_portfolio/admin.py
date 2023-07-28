from django.contrib import admin

from .models import Project


# Register your models here.
@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'title', 'tech_stack', 'libraries', 'year', 'in_progress', 'completed', 'updated']
    list_filter = ['title', 'completed']
    list_editable = ['title', 'completed']
    prepopulated_fields = {'slug': ('title',)}
