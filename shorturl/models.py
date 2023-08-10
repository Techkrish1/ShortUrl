from django.db import models

# Created models 

class urlModel(models.Model):
    longurl = models.CharField(max_length=5000)
    shorturl = models.CharField(max_length=7)
    count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.shorturl