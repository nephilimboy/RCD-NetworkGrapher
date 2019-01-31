from rest_framework import serializers

from grapher.serializer import LogParserSerializer
from grapherEntities.models import GrapherEntityExtraDetails, GrapherEntity


class grapherEntityExtraDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrapherEntityExtraDetails
        fields = ("id", "name", "type")


class grapherEntitySerializer(serializers.ModelSerializer):
    logParsers_list = LogParserSerializer(many=True)
    grapher_entity_extra_details = grapherEntityExtraDetailsSerializer(many=True)

    class Meta:
        model = GrapherEntity
        fields = (
            'id', 'name', 'grapher_entity_extra_details', 'logParsers_list')
