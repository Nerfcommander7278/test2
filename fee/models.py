from django.db import models

# Create your models here.
class post(models.Model):
    text = models.CharField(max_length=140, null = False)

    def __str__(self):
        return self.text