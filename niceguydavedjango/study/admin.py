from django.contrib import admin
from niceguydavedjango.study.models import Department, Specialism
from reversion.admin import VersionAdmin

# =============================================================================

class DepartmentAdmin(VersionAdmin):
    filter_horizontal = ('specialism',)
    list_display = ('name',)


class SpecialismAdmin(VersionAdmin):
    # TODO: work out how to create reciprocal relationship back into Department
    # filter_horizontal = ('department',)
    list_display = ('name',)
    
# -----------------------------------------------------------------------------

admin.site.register(Department, DepartmentAdmin)  
admin.site.register(Specialism, SpecialismAdmin)