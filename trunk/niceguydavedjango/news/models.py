import datetime
from django.db import models

# =============================================================================

class News(models.Model):
    heading             = models.CharField(max_length=255)
    copy                = models.TextField()
    creation_date       = models.DateTimeField(default=datetime.datetime.today())
    active              = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "News"
        
    def __unicode__(self):
        return '%s' % self.heading