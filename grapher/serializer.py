from rest_framework import serializers

from .models import LogParser, CustomPattern, JasonParserAlias, JasonParser, LogParserCrudFormCustomPattern, \
    LogParserCrudFormStaticPattern


class LogParserCrudFormCustomPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogParserCrudFormCustomPattern
        fields = ("id", "order", "parserType", "name", "patternType", "customPatternName")
        # allow_null is for to save object inside update method in JasonParserSerializer
        extra_kwargs = {'id': {'read_only': False, 'allow_null': True},
                        'customPatternName': {'read_only': False, 'allow_null': True}}


class LogParserCrudFormStaticPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogParserCrudFormStaticPattern
        fields = ("id", "order", "parserType", "text")
        # allow_null is for to save object inside update method in JasonParserSerializer
        extra_kwargs = {'id': {'read_only': False, 'allow_null': True},
                        'text': {'read_only': False, 'allow_null': True}}


class LogParserSerializer(serializers.ModelSerializer):
    # id = serializers.PrimaryKeyRelatedField(read_only=True)
    logParser_crudForm_customPattern = LogParserCrudFormCustomPatternSerializer(many=True)
    logParser_crudForm_staticPattern = LogParserCrudFormStaticPatternSerializer(many=True)

    class Meta:
        model = LogParser
        # fields = '__all__'
        fields = (
            'id', 'name', 'pattern', 'totalPattern', 'logParser_crudForm_customPattern',
            'logParser_crudForm_staticPattern')

    def create(self, validated_data):
        logParser_crudForm_customPattern_data = validated_data.pop('logParser_crudForm_customPattern')
        logParser_crudForm_staticPattern_data = validated_data.pop('logParser_crudForm_staticPattern')
        logParser = LogParser.objects.create(**validated_data)
        for logParser_customPattern in logParser_crudForm_customPattern_data:
            customPattern = LogParserCrudFormCustomPattern.objects.get_or_create(logParser=logParser,
                                                                                 **logParser_customPattern)

        for logParser_staticPattern in logParser_crudForm_staticPattern_data:
            staticPattern = LogParserCrudFormStaticPattern.objects.get_or_create(logParser=logParser,
                                                                                 **logParser_staticPattern)

        logParser.save()
        return logParser

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.pattern = validated_data.get('pattern', instance.pattern)
        instance.totalPattern = validated_data.get('totalPattern', instance.totalPattern)

        # delete custom pattern which is not presented in the input jason
        for current_customPattern in instance.logParser_crudForm_customPattern.all():
            isInstanceAvailable = False
            for logParser_crudForm_customPattern_valid_data in validated_data['logParser_crudForm_customPattern']:
                if current_customPattern.id == logParser_crudForm_customPattern_valid_data.get('id', None):
                    isInstanceAvailable = True
                    break
            if not isInstanceAvailable:
                current_customPattern.delete()

        # delete static pattern which is not presented in the input jason
        for current_staticPattern in instance.logParser_crudForm_staticPattern.all():
            isInstanceAvailable = False
            for logParser_crudForm_staticPattern_valid_data in validated_data['logParser_crudForm_staticPattern']:
                if current_staticPattern.id == logParser_crudForm_staticPattern_valid_data.get('id', None):
                    isInstanceAvailable = True
                    break
            if not isInstanceAvailable:
                current_staticPattern.delete()

        # Custom pattern
        for logParser_crudForm_customPattern_valid_data in validated_data['logParser_crudForm_customPattern']:
            logParser_crudForm_customPattern_valid_data_id = logParser_crudForm_customPattern_valid_data.get('id', None)
            if logParser_crudForm_customPattern_valid_data_id:
                logParser_crudForm_customPattern_original = LogParserCrudFormCustomPattern.objects.get(
                    pk=logParser_crudForm_customPattern_valid_data_id)
                logParser_crudForm_customPattern_original.order = logParser_crudForm_customPattern_valid_data.get(
                    'order', None)
                logParser_crudForm_customPattern_original.parserType = logParser_crudForm_customPattern_valid_data.get(
                    'parserType', None)
                logParser_crudForm_customPattern_original.name = logParser_crudForm_customPattern_valid_data.get('name',
                                                                                                                 None)
                logParser_crudForm_customPattern_original.patternType = logParser_crudForm_customPattern_valid_data.get(
                    'patternType', None)
                logParser_crudForm_customPattern_original.customPatternName = logParser_crudForm_customPattern_valid_data.get(
                    'customPatternName', None)
                logParser_crudForm_customPattern_original.save()
            else:
                logParser_crudForm_customPattern_new = LogParserCrudFormCustomPattern.objects.create(logParser=instance,
                                                                                                     **logParser_crudForm_customPattern_valid_data)
                logParser_crudForm_customPattern_new.save()
                instance.logParser_crudForm_customPattern.add(logParser_crudForm_customPattern_new)

        # Static pattern
        for logParser_crudForm_staticPattern_valid_data in validated_data['logParser_crudForm_staticPattern']:
            logParser_crudForm_staticPattern_valid_data_id = logParser_crudForm_staticPattern_valid_data.get('id', None)
            if logParser_crudForm_staticPattern_valid_data_id:
                logParser_crudForm_staticPattern_original = LogParserCrudFormStaticPattern.objects.get(
                    pk=logParser_crudForm_staticPattern_valid_data_id)
                logParser_crudForm_staticPattern_original.order = logParser_crudForm_staticPattern_valid_data.get(
                    'order', None)
                logParser_crudForm_staticPattern_original.parserType = logParser_crudForm_staticPattern_valid_data.get(
                    'parserType', None)
                logParser_crudForm_staticPattern_original.text = logParser_crudForm_staticPattern_valid_data.get('text',
                                                                                                                 None)
                logParser_crudForm_staticPattern_original.save()
            else:
                logParser_crudForm_staticPattern_new = LogParserCrudFormStaticPattern.objects.create(logParser=instance,
                                                                                                     **logParser_crudForm_staticPattern_valid_data)
                logParser_crudForm_staticPattern_new.save()
                instance.logParser_crudForm_staticPattern.add(logParser_crudForm_staticPattern_new)

        instance.save()
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

        # delete alias which is not presented in the input jason
        for current_alias in instance.jason_alias.all():
            isInstanceAvailable = False
            for jason_alias_valid_data in validated_data['jason_alias']:
                if current_alias.id == jason_alias_valid_data.get('id', None):
                    isInstanceAvailable = True
                    break
            if not isInstanceAvailable:
                current_alias.delete()

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
