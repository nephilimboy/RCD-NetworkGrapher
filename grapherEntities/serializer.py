from rest_framework import serializers

from grapher.models import LogParser
from grapher.serializer import LogParserSerializer
from grapherEntities.models import GrapherEntity


class grapherEntitySerializer(serializers.ModelSerializer):
    logParser_list = LogParserSerializer(many=True)

    class Meta:
        model = GrapherEntity
        fields = (
            'id', 'name', 'jasonData', 'logParser_list')

    def create(self, validated_data):
        logParsers_list_data = validated_data.pop('logParser_list')
        grapherEntity = GrapherEntity.objects.create(**validated_data)
        grapherEntity.save()
        for logParsers in logParsers_list_data:
            logParser = LogParser.objects.get_or_create(name=logParsers['name'])[0]
            grapherEntity.logParser_list.add(logParser)

        return grapherEntity
