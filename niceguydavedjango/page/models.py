import datetime
from django.db import models

# =============================================================================

class Page(models.Model):
    title               = models.CharField(max_length=100)    
    copy                = models.TextField(blank=True)
    creation_date       = models.DateTimeField(default=datetime.datetime.today())
    active              = models.BooleanField(default=True)
    
    def __unicode__(self):
        return '%s' % self.title
    
    
