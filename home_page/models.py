from django.db import models

# Create your models here.
class Response(models.Model):
    boolean_value = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Response: {self.boolean_value}'

class DataEntry(models.Model):
    boolean_value = models.BooleanField()

    def __str__(self):
        return str(self.boolean_value)