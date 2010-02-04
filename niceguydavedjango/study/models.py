from django.db import models

# =============================================================================

class Specialism(models.Model):
    name = models.CharField(max_length=100)
    
# TODO: think about pulling all these choices out into a separate config file
DEPT_CHOICES = (
    ('Accordion', 'Accordion'),
    ('Brass', 'Brass'),
    ('Choral', 'Choral Conducting'),
    ('Composition', 'Composition'),
    ('Conducting', 'Conducting'),
    ('Guitar', 'Guitar'),
    ('Harp', 'Harp'),
    ('Historical', 'Historical Performance'),
    ('Jazz', 'Jazz'),
    ('MusicalTheatre', 'Musical Theatre'),
    ('Opera', 'Opera'),
    ('Organ', 'Organ'),
    ('Piano', 'Piano'),
    ('Strings', 'Strings'),
    ('Timpani_Percussion', 'Timpani and Percussion'),
    ('Vocal', 'Vocal'),
    ('Woodwind', 'Woodwind'),
)
class Department(models.Model):
    name        = models.CharField(max_length=50, choices=DEPT_CHOICES)
    specialism  = models.ManyToManyField(Specialism, blank=True)