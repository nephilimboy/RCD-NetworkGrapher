from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import LogParser, CustomPattern, JasonParser
from .serializer import LogParserSerializer, CustomPatternSerializer, JasonParserSerializer


class LogParserView(APIView):

    def get(self, format=None):
        """
        Get all the student records
        :param format: Format of the student records to return to
        :return: Returns a list of student records
        """
        logParser = LogParser.objects.all()
        serializer = LogParserSerializer(logParser, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LogParserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        serializer = LogParserSerializer(get_object_or_404(LogParser, pk=pk), data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        (get_object_or_404(LogParser, pk=pk)).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomPatternView(APIView):

    def get(self, format=None):
        customPattern = CustomPattern.objects.all()
        serializer = CustomPatternSerializer(customPattern, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomPatternSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        serializer = CustomPatternSerializer(get_object_or_404(CustomPattern, pk=pk), data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        (get_object_or_404(CustomPattern, pk=pk)).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JasonParserView(APIView):

    def get(self, format=None):
        jasonParser = JasonParser.objects.all()
        serializer = JasonParserSerializer(jasonParser, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JasonParserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        serializer = JasonParserSerializer(get_object_or_404(JasonParser, pk=pk), data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        (get_object_or_404(JasonParser, pk=pk)).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
