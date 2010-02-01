from django.contrib import admin
from niceguydavedjango.person.models import Person

# =============================================================================

class PersonAdmin(admin.ModelAdmin):
    field_sets = [
        (None,                {'fields': ['name']}),
        (None,                {'fields': ['copy']}),
        ('Date information',  {'fields': ['creation_date'], 
                               'classes': ['collapse']})
    ]
    list_display = ('email','first_name','last_name',)
admin.site.register(Person, PersonAdmin)

