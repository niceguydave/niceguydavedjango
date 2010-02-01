import datetime
from django.db import models

# =============================================================================

class News(models.Model):
    heading             = models.CharField(max_length=255)
    copy                = models.TextField()
    creation_date_time  = models.DateTimeField(default=datetime.date.today())
    active              = models.BooleanField(default=True)
    
    def __unicode__(self):
        return '%s' % self.heading