from django.db import models

# =============================================================================

class Specialism(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return u'<Specialism: %s>' % self.name
    
# ------------------------------------------------------------------------------

class Department(models.Model):
    name        = models.CharField(max_length=50, unique=True)
    specialism  = models.ManyToManyField(Specialism, blank=True)
    
    class Meta:
        ordering = ('name',)
    
    def __unicode__(self):
        return u'<Dept: %s>' % self.name