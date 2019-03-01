from django.contrib import admin

# Register your models here.
from grapher.models import LogParser, CustomPattern, JasonParserAlias, JasonParser, LogParserCrudFormCustomPattern, \
    LogParserCrudFormStaticPattern
from grapherEntities.models import GrapherEntity

admin.register(LogParser)(admin.ModelAdmin)
admin.register(LogParserCrudFormCustomPattern)(admin.ModelAdmin)
admin.register(LogParserCrudFormStaticPattern)(admin.ModelAdmin)
admin.register(CustomPattern)(admin.ModelAdmin)
admin.register(JasonParser)(admin.ModelAdmin)
admin.register(JasonParserAlias)(admin.ModelAdmin)

admin.register(GrapherEntity)(admin.ModelAdmin)


