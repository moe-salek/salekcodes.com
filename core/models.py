from django.db import models


# Create your models here.


class Sample(models.Model):
    number = models.IntegerField(default=3)
