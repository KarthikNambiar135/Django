from django.db import models

SHIFTS = [
    ('1', 'Morning'),
    ('2', 'Noon'),
    ('3', 'Night'),
]

# Create your models here.
class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text="Enter the exact time!")