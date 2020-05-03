from django.db import models


# Create your models here.
class ZenoModel(models.Model):
    csv_id = models.CharField(max_length=50, null=True, blank=True, default='')
    csv_temperature = models.CharField(max_length=50, null=True, blank=True, default='')
    csv_timestamp = models.CharField(max_length=50, null=True, blank=True, default='')
    csv_duration = models.CharField(max_length=50, null=True, blank=True, default='')

    def __str__(self):
        return self.csv_id


class GetRequestActivityLog(models.Model):
    method = models.CharField(max_length=6)
    url = models.CharField(max_length=1024)
    timeStamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Request'
