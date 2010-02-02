from django.contrib import admin
from niceguydavedjango.testimonial.models import Testimonial
from reversion.admin import VersionAdmin

# =============================================================================

class TestimonialAdmin(VersionAdmin):
    list_display = ('name','creation_date')
admin.site.register(Testimonial, TestimonialAdmin)

