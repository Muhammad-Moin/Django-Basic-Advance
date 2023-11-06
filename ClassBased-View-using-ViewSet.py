from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Course, CourseSerilizers
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics
from rest_framework.viewsets import ViewSet

class CourseListView(ViewSet):
    def list(self, request):
        course = Course.objects.all()
        courseSerilizers = CourseSerilizers(course, many=True)
        return Response(courseSerilizers.data)

    def create(self, request):
        courseSerilizers = CourseSerilizers(data=request.data)
        if courseSerilizers.is_valid():
            courseSerilizers.save()
            return Response({"message": "Course created successfully."},status=201 )
        else:
            return Response(courseSerilizers.errors)
        
    def retrieve(self, request, pk=None):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404("Course does not exist")

        courseSerializer = CourseSerilizers(course)
        return Response(courseSerializer.data)
    
    def destroy(self, request, pk=None):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response({'message':'Successfully deleted'})
    
    def update(self, request, pk=None):
        course = Course.objects.get(pk=pk)
        courseSerilizers = CourseSerilizers(course,data=request.data)
        if courseSerilizers.is_valid():
            courseSerilizers.save()
            return Response({"message": "Course created successfully."},status=201 )
        else:
            return Response(courseSerilizers.errors)
