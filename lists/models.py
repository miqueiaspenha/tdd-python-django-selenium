from django.db import models


class Item(models.Model):
    # TODO - Aceitar mais de uma lista
    text = models.TextField(default="")
