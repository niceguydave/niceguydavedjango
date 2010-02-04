from django.contrib import admin
from niceguydavedjango.person.models import Student, Staff, VisitingGuest
from reversion.admin import VersionAdmin

# =============================================================================

class StudentAdmin(VersionAdmin):
    pass
    list_display = ('email','first_name','last_name',)

class StaffAdmin(VersionAdmin):
    list_display = ('email','first_name','last_name',)

class VisitingGuestAdmin(VersionAdmin):
    field_sets = [
        ('Name',              {'fields': ['first_name','last_name']}),        
        ('Date information',  {'fields': ['creation_date'], 
                               'classes': ['collapse']})
    ]
    list_display = ('first_name','last_name','qualifications','title')

admin.site.register(Student, StudentAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(VisitingGuest, VisitingGuestAdmin)