from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(models.Job)
class JobAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'last_run', 'next_run','schedule_type']
    search_fields = ['name']