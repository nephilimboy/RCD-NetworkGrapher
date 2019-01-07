from rest_framework import serializers

from .models import LogParser, CustomPattern


class LogParserSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = LogParser
        fields = '__all__'
        # fields = ('id', 'name', 'pattern')

    def create(self, validated_data):
        instance = LogParser.objects.create(**validated_data)
        return instance


class CustomPatternSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CustomPattern
        fields = '__all__'
        # fields = ('id', 'name', 'pattern')

    def create(self, validated_data):
        instance = CustomPattern.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.pattern = validated_data.get('pattern', instance.pattern)
        instance.save()
        return instance
