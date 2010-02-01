import datetime
from django.db import models

# =============================================================================

class PageType(models.Model):
    name                = models.CharField(max_length=20)
    description         = models.CharField(max_length=100)


class Page(models.Model):
    title               = models.CharField(max_length=100)    
    copy                = models.TextField(required=False)
    seo_title           = models.CharField(max_length=128)
    seo_description     = models.CharField(max_length=256)
    seo_keywords        = models.CharField(max_length=256)
    active              = models.BooleanField(default=True)
    
    page_type           = models.ForeignKey(PageType)
    
    def __unicode__(self):
        return '%s' % self.title
    
    
