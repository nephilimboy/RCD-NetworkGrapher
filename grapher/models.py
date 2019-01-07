from django.db import models


class LogParser(models.Model):
    name = models.CharField(max_length=50)
    pattern = models.TextField()

    def __str__(self):
        return self.name + ' ' + self.pattern


class CustomPattern(models.Model):
    name = models.CharField(max_length=50)
    pattern = models.TextField()

    def __str__(self):
        return self.name + ' ' + self.pattern
