from django.db import models

SHORT_LENGTH = 10
LONG_LENGTH = 100


class Crop(models.Model):
    """
        This will represent each crop
    """
    name = models.CharField(max_length=SHORT_LENGTH)
    description = models.TextField(max_length=LONG_LENGTH, blank=True)
    file = models.FileField(upload_to='/crops/')
