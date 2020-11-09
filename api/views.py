from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

from .models import *
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Question1-List': '/question1-list/',
		'Question1-Create': '/question1-create/',
		'Question2-List': '/question2-list/',
		'Question2-Create': '/question2-create/',
		}

	return Response(api_urls)

@api_view(['GET'])
def question1List(request):
	tasks = Question1.objects.all().order_by('-id')
	serializer = Question1Serializer(tasks, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def question1Create(request):
	serializer = Question1Serializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['GET'])
def question2List(request):
	tasks = Question2.objects.all().order_by('-id')
	serializer = Question2Serializer(tasks, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def question2Create(request):
	serializer = Question2Serializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)
# @api_view(['POST'])
# def taskUpdate(request, pk):
# 	task = Question1.objects.get(id=pk)
# 	serializer = TaskSerializer(instance=task, data=request.data)
#
# 	if serializer.is_valid():
# 		serializer.save()
#
# 	return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def taskDelete(request, pk):
# 	task = Question1.objects.get(id=pk)
# 	task.delete()
#
# 	return Response('Item succsesfully delete!')



