from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Course, CourseSerilizers
from rest_framework.views import APIView
from django.http import Http404

# Class Based View

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        courseSerilizers = CourseSerilizers(courses,many=True)
        return Response(courseSerilizers.data)
    
    def post(self, request):        
        courseSerilizers = CourseSerilizers(data=request.data)
        if courseSerilizers.is_valid():
            courseSerilizers.save()
            return Response(courseSerilizers.data)
        return Response(courseSerilizers.errors)
    
class CourseDetailView(APIView):
    def getCourse(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404("Course does not exist")
    def get(self,request, pk):
        course = self.getCourse(pk)
        courseSerilizers = CourseSerilizers(course)
        return Response(courseSerilizers.data)
        
    def delete(self, request, pk):
        course = self.getCourse(pk)
        course.delete()
        return Response({'message':'Deleted'})
    
    def put(self, request, pk):
        course = self.getCourse(pk)
        courseSerilizers = CourseSerilizers(instance=course, data=request.data)
        if courseSerilizers.is_valid():
            courseSerilizers.save()
            return Response( courseSerilizers.data)
        return  Response(courseSerilizers.errors)
        
            
# Function Based View


# Create your views here.
@api_view(['GET','POST'])
def courseListView(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        courseSerilizers = CourseSerilizers(courses,many=True)
        return Response(courseSerilizers.data)
         
    elif request.method == 'POST':
        courseSerilizers = CourseSerilizers(data=request.data)
        if  courseSerilizers.is_valid():
            courseSerilizers.save()
            return Response(courseSerilizers.data)
        else:
            return Response(courseSerilizers.errors)
        

@api_view(['GET','DELETE','PUT'])
def courseDetailView(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        courseSerilizers = CourseSerilizers(course)
        return Response(courseSerilizers.data)
    
    elif request.method == 'PUT':
        courseSerilizers = CourseSerilizers(course,data=request.data)
        if courseSerilizers.is_valid():
            courseSerilizers.save()
            return Response(courseSerilizers.data)
        return Response(courseSerilizers.errors)
    
    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
