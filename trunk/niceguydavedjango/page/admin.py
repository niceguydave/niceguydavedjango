from django.contrib import admin
from niceguydavedjango.page.models import Page

# =============================================================================

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','creation_date',)
admin.site.register(Page, PageAdmin)

