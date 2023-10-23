from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import sports
from . serializers import sportsSerializer

class sport(APIView):                  # inherits from an APIView
    def post(self, request):
        data = request.data             # Data passed in body
        serializer = sportsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()           # to do post request
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) # if error

    def get(self, request, id=None):
        if id:
            item = sports.objects.get(id=id)
            serializer = sportsSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        items = sports.objects.all()
        serializer = sportsSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, id=None):
        data = request.data            # Data passed to overwrite
        instance =sports.objects.get(id=id)
        serializer = sportsSerializer(instance, data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    def delete(self, request, id=None):
        instance = sports.objects.get(id=id)
        serializer = sportsSerializer(instance)
        instance.delete()
        return Response(serializer.data)