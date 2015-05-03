from django.db import models

# Create your models here.

class Machine_Learning_Models(models.Model):
    name = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    example_code = models.TextField(blank=True)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.name
