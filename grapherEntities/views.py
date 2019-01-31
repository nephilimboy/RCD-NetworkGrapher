from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from grapherEntities.models import GrapherEntity
from grapherEntities.serializer import grapherEntitySerializer


class grapherEntityView(APIView):

    def get(self, format=None):
        grapherEntity = GrapherEntity.objects.all()
        serializer = grapherEntitySerializer(grapherEntity, many=True)
        return Response(serializer.data)



