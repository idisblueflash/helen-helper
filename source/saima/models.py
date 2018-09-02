from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)


class Command(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    command = models.CharField(max_length=200)

