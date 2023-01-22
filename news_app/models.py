from django.db import models


class TodayFeed(models.Model):
    title = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=600,null=True, blank=True)
    date = models.CharField(max_length=60, null=True, blank=True)
    time_fetched = models.DateTimeField(auto_now_add=True, null=True,blank=True)

    def __str__(self):
        return self.title


