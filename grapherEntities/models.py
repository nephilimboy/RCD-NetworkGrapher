from django.db import models

from grapher.models import LogParser


class GrapherEntity(models.Model):
    name = models.CharField(max_length=50)
    logParser_list = models.ManyToManyField(LogParser, related_name="logParsers_list", blank=True)

    def __str__(self):
        return self.name


class GrapherEntityExtraDetails(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=200)
    grapherEntity = models.ForeignKey(GrapherEntity, on_delete=models.CASCADE,
                                      related_name="grapher_entity_extra_details")

    def __str__(self):
        return self.name + ' ' + self.type + ' '
