from django.db import models

class Kpi(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    savingtime = models.FloatField()
    size = models.IntegerField()

    def __str__(self):
        return self.name