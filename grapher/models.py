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


class JasonParser(models.Model):
    name = models.CharField(max_length=50)
    jason = models.TextField()

    def __str__(self):
        return self.name + ' ' + self.jason


class JasonParserAlias(models.Model):
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=200)
    jasonParser = models.ForeignKey(JasonParser, on_delete=models.CASCADE, related_name="jason_alias")

    def __str__(self):
        return self.name + ' ' + self.path
