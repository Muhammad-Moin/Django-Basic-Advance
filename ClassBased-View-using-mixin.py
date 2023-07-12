from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Course, CourseSerilizers
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics

class CourseListView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerilizers

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request=request)

class CourseDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    # retrive single primary data  mixins.RetrieveModelMixin
    # delete single primary data  mixins.DestroyModelMixin
    # update single primary data   mixins.UpdateModelMixin
    queryset = Course.objects.all()
    serializer_class = CourseSerilizers

    def get(self, request, pk):
        return self.retrieve(request,pk)
        
    
    def put(self, request, pk):
        return self.update(request,pk)

    def delete(self, request, pk):
        return self.destroy(request,pk)
