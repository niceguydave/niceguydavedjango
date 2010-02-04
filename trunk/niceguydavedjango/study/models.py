from django.db import models

# =============================================================================

class Specialism(models.Model):
    name = models.CharField(max_length=100)
    
    
class Department(models.Model):
    name        = models.CharField(max_length=100)
    specialism  = models.ManyToManyField(Specialism, blank=True)