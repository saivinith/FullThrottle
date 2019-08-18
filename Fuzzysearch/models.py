from django.db import models

# Create your models here.
class Words(models.Model):

    class Meta:
        db_table = 'Words'

    word = models.CharField(max_length=12, blank=True, default=None)
    frequency = models.IntegerField(blank=True, default=None)