from django.db import models

from grapherEntities.models import GrapherEntity


class LogParser(models.Model):
    name = models.CharField(max_length=50)
    pattern = models.TextField()
    totalPattern = models.IntegerField(null=True)
    grapherEntity = models.ManyToManyField(GrapherEntity, related_name="logParsers_list", blank=True)

    def __str__(self):
        return self.name + ' ' + self.pattern


class LogParserCrudFormCustomPattern(models.Model):
    order = models.CharField(max_length=50)
    parserType = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    patternType = models.CharField(max_length=50)
    customPatternName = models.CharField(max_length=50, null=True, blank=True)
    logParser = models.ForeignKey(LogParser, on_delete=models.CASCADE, related_name="logParser_crudForm_customPattern")

    def __str__(self):
        return self.order + ' ' + self.parserType + ' ' + self.name + ' ' + self.patternType + ' ' + self.customPatternName


class LogParserCrudFormStaticPattern(models.Model):
    order = models.CharField(max_length=50)
    parserType = models.CharField(max_length=50)
    text = models.TextField(null=True, blank=True)
    logParser = models.ForeignKey(LogParser, on_delete=models.CASCADE, related_name="logParser_crudForm_staticPattern")

    def __str__(self):
        return self.order + ' ' + self.parserType + ' ' + self.text


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
