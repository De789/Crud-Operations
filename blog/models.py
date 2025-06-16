from datetime import timezone
from django.db import models

# Create your models here.
class CustomerReportRecord(models.Model):
    time_raised = models.DateTimeField()
    reference = models.CharField(unique=True, max_length=20)
    description = models.TextField()