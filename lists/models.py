from django.db import models


class List(models.Model):
    pass


class Item(models.Model):
    # TODO - Aceitar mais de uma lista
    text = models.TextField(default="")
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)
