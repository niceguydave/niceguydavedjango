from django.contrib import admin
from niceguydavedjango.person.models import Person

# =============================================================================

class PersonAdmin(admin.ModelAdmin):
    list_display = ('email')
admin.site.register(Person, PersonAdmin)

