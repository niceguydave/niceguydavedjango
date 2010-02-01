import datetime
from django.db import models

# =============================================================================

class Person(models.Model):
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    email           = models.EmailField()
    creation_date   = models.DateTimeField(default=datetime.datetime.today())
    active          = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "People"
    
    def __unicode__(self):
        return '%s' % self.email

