from django.contrib import admin
from niceguydavedjango.study.models import Department
from reversion.admin import VersionAdmin

# =============================================================================

class DepartmentAdmin(VersionAdmin):
    pass
admin.site.register(Department, DepartmentAdmin)