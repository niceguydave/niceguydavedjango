from django.contrib import admin
from niceguydavedjango.study.models import Department, Specialism
from reversion.admin import VersionAdmin

# =============================================================================

class DepartmentAdmin(VersionAdmin):
    list_display = ('name',)

class SpecialismAdmin(VersionAdmin):
    # this will get a horizontal sorting bar working
    # filter_horizontal = ['department']
    list_display = ('name',)
    
# -----------------------------------------------------------------------------

admin.site.register(Department, DepartmentAdmin)  
admin.site.register(Specialism, SpecialismAdmin)