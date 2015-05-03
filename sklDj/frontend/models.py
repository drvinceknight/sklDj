from django.db import models

# Create your models here.

class Machine_Learning_Models(models.Model):
    name = models.CharField(blank=True, max_length=200)
    enw = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True)
    disgrifiad = models.TextField(blank=True)
    link = models.URLField(blank=True)
    slug = models.CharField(max_length=200)
    example_code = models.TextField(blank=True)

    def __str__(self):
        return self.name
