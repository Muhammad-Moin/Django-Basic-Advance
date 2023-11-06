from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Course, CourseSerilizers
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics

# If you want two or more than two consecutive class use like get and post or get and update or get, update, and delete
# generics.RetrieveUpdateAPIView,generics.RetrieveUpdateDestroyAPIView,generics.RetrieveUpdateDestroyAPIView
class CourseListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerilizers

class CourseDetailView(generics.RetrieveAPIView,generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerilizers
