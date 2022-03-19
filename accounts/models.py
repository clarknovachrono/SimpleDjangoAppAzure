from django.db import models

# Create your models here.


class Personal(models.Model):
    image_url = models.CharField(max_length=2048, null=True, blank=True, default="")
    name = models.CharField(max_length=255, null=True, blank=True)
    course = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(max_length=1)

    def __str__(self):
        return self.name

