import datetime
from django.db import models
from niceguydavedjango.study.models import Department

# =============================================================================

class Person(models.Model):
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    email           = models.EmailField()
    creation_date   = models.DateTimeField(default=datetime.datetime.today())
    active          = models.BooleanField(default=True)
    
    department      = models.ManyToManyField(Department, blank=True)
    
    def __unicode__(self):
        return '<Person: %s>' % self.email

# ------------------------------------------------------------------------------    

class Staff(Person):
    title           = models.CharField(max_length=100)
    qualifications  = models.CharField(max_length=100, blank=True)    
    
    class Meta:
        verbose_name_plural = "Staff"
    
    def __unicode__(self):
        return '<Staff: %s>' % self.email
    
# ------------------------------------------------------------------------------

class VisitingGuest(Staff):
    bio             = models.TextField(blank=True)
    class Meta:
        verbose_name_plural = "Visiting Guests"

    def __unicode__(self):
        return '<Visiting Guest: %s>' % self.email

# ------------------------------------------------------------------------------

class Student(Person):
    def __unicode__(self):
        return '<Student: %s>' % self.email

