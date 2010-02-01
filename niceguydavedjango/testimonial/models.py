import datetime
from django.db import models
from niceguydavedjango.person.models import Person

# =============================================================================

class Testimonial(models.Model):
    name                = models.CharField(max_length=50)
    copy                = models.TextField()
    creation_date       = models.DateTimeField(default=datetime.datetime.today())
    active              = models.BooleanField(default=True)
    
    people              = models.ManyToManyField(Person, blank=True)
    
    def __unicode__(self):
        return '%s' % self.name
