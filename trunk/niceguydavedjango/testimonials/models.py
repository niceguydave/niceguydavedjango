import datetime
from django.db import models

# =============================================================================

class Testimonial(models.Model):
    name                = models.CharField(max_length=50)
    copy                = models.TextField()
    creation_date_time  = models.DateTimeField(default=datetime.date.today())
    active              = models.BooleanField(default=True)
    
    def __unicode__(self):
        return '%s' % self.name
