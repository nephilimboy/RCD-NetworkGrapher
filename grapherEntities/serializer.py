from rest_framework import serializers

from grapher.models import LogParser
from grapher.serializer import LogParserSerializer
from grapherEntities.models import GrapherEntityExtraDetails, GrapherEntity


class grapherEntityExtraDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrapherEntityExtraDetails
        fields = ("id", "name", "type")


class grapherEntitySerializer(serializers.ModelSerializer):
    logParser_list = LogParserSerializer(many=True)
    grapher_entity_extra_details = grapherEntityExtraDetailsSerializer(many=True)

    class Meta:
        model = GrapherEntity
        fields = (
            'id', 'name', 'grapher_entity_extra_details', 'logParser_list')

    def create(self, validated_data):
        logParsers_list_data = validated_data.pop('logParser_list')
        grapher_entity_extra_details_data = validated_data.pop('grapher_entity_extra_details')
        grapherEntity = GrapherEntity.objects.create(**validated_data)
        grapherEntity.save()
        for logParsers in logParsers_list_data:
            logParser = LogParser.objects.get_or_create(name=logParsers['name'])[0]
            grapherEntity.logParser_list.add(logParser)

        for grapher_entity_extra_detail in grapher_entity_extra_details_data:
            grapherEntityExtraDetails = GrapherEntityExtraDetails.objects.get_or_create(grapherEntity=grapherEntity,
                                                                                        **grapher_entity_extra_detail)

        return grapherEntity
