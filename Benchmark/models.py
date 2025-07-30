from django.db import models
from AIT.models import AIT


class Benchmark(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    description = models.CharField(max_length=255, default='')
    men = models.IntegerField()
    women = models.IntegerField()
    girls = models.IntegerField()
    boys = models.IntegerField()
    disabled = models.IntegerField()
    ait = models.ForeignKey(AIT, on_delete=models.CASCADE, related_name='benchmarks')