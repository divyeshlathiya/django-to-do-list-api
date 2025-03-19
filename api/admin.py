from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title","description")
    list_filter = ("completed",)
    search_fields = ("title","description")
    ordering = ("due_date",)
    