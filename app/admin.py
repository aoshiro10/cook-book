from django.contrib import admin
from .models import Recipe

from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Recipe)
class ViewAdmin(ImportExportModelAdmin):
	pass