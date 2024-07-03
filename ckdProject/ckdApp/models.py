from django.db import models

# Create your models here.
class ckdModel(models.Model):



    Age = models.FloatField()
    # Age=models.IntegerField()
    Experience = models.FloatField()
    Income  =models.FloatField()
    Family = models.FloatField()
    CCAvg = models.FloatField()
    Education = models.FloatField()
    Mortgage = models.FloatField()
    CDAccount = models.FloatField()
    OnlineAccount = models.FloatField()

    def __str__(self):
        return str(self.pk)
