from django.db import models


# Create your models here.

class DataEntry(models.Model):
    boolean_value = models.BooleanField()

    def __str__(self):
        return str(self.boolean_value)
