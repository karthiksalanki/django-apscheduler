from django.db import models

# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length=255)
    last_run = models.DateTimeField(null=True, blank=True)
    next_run = models.DateTimeField(null=True, blank=True)
    schedule_type = models.CharField(max_length=50)  # e.g., interval, cron
    schedule_details = models.JSONField()  # Store specific schedule details