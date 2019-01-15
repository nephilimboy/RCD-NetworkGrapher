from rest_framework import serializers

from .models import LogParser, CustomPattern, JasonParserAlias, JasonParser


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

    def create(self, validated_data):
        instance = CustomPattern.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.pattern = validated_data.get('pattern', instance.pattern)
        instance.save()
        return instance


class JasonParserAliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = JasonParserAlias
        fields = ("id", "name", "path")
        # allow_null is for to save object inside update method in JasonParserSerializer
        extra_kwargs = {'id': {'read_only': False, 'allow_null': True}}


class JasonParserSerializer(serializers.ModelSerializer):
    jason_alias = JasonParserAliasSerializer(many=True)

    class Meta:
        model = JasonParser
        fields = ("id", "name", "jason", "jason_alias")

    def create(self, validated_data):
        jason_alias_data = validated_data.pop('jason_alias')
        jasonParser = JasonParser.objects.create(**validated_data)
        for jason_alias in jason_alias_data:
            jason_alias, created = JasonParserAlias.objects.get_or_create(jasonParser=jasonParser, **jason_alias)
        jasonParser.save()
        return jasonParser

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.jason = validated_data.get('jason', instance.jason)

        for jason_alias_valid_data in validated_data['jason_alias']:
            jason_alias_valid_data_id = jason_alias_valid_data.get('id', None)
            if jason_alias_valid_data_id:
                jasonParserAlias_original = JasonParserAlias.objects.get(pk=jason_alias_valid_data_id)
                jasonParserAlias_original.name = jason_alias_valid_data.get('name', None)
                jasonParserAlias_original.path = jason_alias_valid_data.get('path', None)
                jasonParserAlias_original.save()
            else:
                jasonParserAlias_new = JasonParserAlias.objects.create(jasonParser=instance, **jason_alias_valid_data)
                jasonParserAlias_new.save()
                instance.jason_alias.add(jasonParserAlias_new)

        instance.save()
        return instance
