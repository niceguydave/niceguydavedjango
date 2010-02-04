import datetime
from django.db import models

# =============================================================================

TYPE_CHOICES = (
    ('Student', 'Student'),
    ('Staff', 'Staff'),
    ('Guest', 'Visiting guest'),
)

class Person(models.Model):
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    email           = models.EmailField()
    person_type     = models.CharField(max_length=10, choices=TYPE_CHOICES)
    creation_date   = models.DateTimeField(default=datetime.datetime.today())
    active          = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "People"
    
    def __unicode__(self):
        return '%s' % self.email

