from django.db import models


class Image(models.Model):
    image = models.ImageField(
        upload_to=games, height_field=None, width_field=None, max_length=None)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
