from django.db import models


class Review(models.Model):
    content = models.CharField(max_length=255
    player=models.ForeignKey("Player", on_delete=models.CASCADE)
