from django.db import models


# Create your models here.

class GrapherEntity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class GrapherEntityExtraDetails(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=200)
    grapherEntity = models.ForeignKey(GrapherEntity, on_delete=models.CASCADE,
                                      related_name="grapher_entity_extra_details")

    def __str__(self):
        return self.name + ' ' + self.type + ' '
