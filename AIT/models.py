from django.db import models
from Project.models import Project
 
class AIT(models.Model): 
    activity  = models.CharField(max_length=255, blank=False, default='')
    indicator = models.CharField(max_length=255, blank=False, default='')
    target    = models.CharField(max_length=255, blank=False, default='')
    project   = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='aits')

    def __str__(self):
        return f"{self.activity}  {self.indicator}  {self.target}"


 