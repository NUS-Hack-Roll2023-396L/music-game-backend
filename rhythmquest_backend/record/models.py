from django.db import models
from django.contrib.auth.models import User


class MusicRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_file = models.FileField(upload_to="recordings/")
    score = models.IntegerField()
