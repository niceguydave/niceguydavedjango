from django.contrib import admin
from niceguydavedjango.news.models import News
from reversion.admin import VersionAdmin

# =============================================================================

class NewsAdmin(VersionAdmin):
    pass
admin.site.register(News, NewsAdmin)

