from django.db import models

class Creator(models.Model):
    name = models.CharField(max_length=100)
    profile_url = models.URLField()

class Prezi(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.URLField()
    created_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
