from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from grapherEntities.models import GrapherEntity
from grapherEntities.serializer import grapherEntitySerializer


class grapherEntityView(APIView):

    def get(self, format=None):
        grapherEntity = GrapherEntity.objects.all()
        serializer = grapherEntitySerializer(grapherEntity, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = grapherEntitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)
