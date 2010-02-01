from django.contrib import admin
from niceguydavedjango.testimonial.models import Testimonial

# =============================================================================

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name','creation_date')
admin.site.register(Testimonial, TestimonialAdmin)

