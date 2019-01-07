from django.contrib import admin

# Register your models here.
from grapher.models import LogParser, CustomPattern

admin.register(LogParser)(admin.ModelAdmin)
admin.register(CustomPattern)(admin.ModelAdmin)