from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from appi.models import Appi
from appi.serializers import AppiSerializer


@csrf_exempt
def appi_list(request):
    if request.method == 'GET':
        appi = Appi.objects.all()
        serializer = AppiSerializer(appi, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AppiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def appi_detail(request, pk):
    try:
        appi = Appi.objects.get(pk=pk)
    except Appi.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AppiSerializer(appi)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AppiSerializer(appi, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        appi.delete()
        return HttpResponse(status=204)