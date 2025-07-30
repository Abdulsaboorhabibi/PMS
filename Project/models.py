from django.db import models
from django.utils import timezone

class Project(models.Model):
    """
    Django model representing a Project.
    """
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    province = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        # Define the ordering and other metadata for the model
        ordering = ['title']
