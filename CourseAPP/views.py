from django.shortcuts import render
from django.http import HttpResponse
from .serializers import CourseSerializer
from .models import Course
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework import mixins
# Create your views here.

class CourseList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    queryset=Course.objects.all()
    serializer_class=CourseSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class CourseDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

    queryset=Course.objects.all()
    serializer_class=CourseSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)


"""
class CourseList(APIView):

    def get(self,request):
       courses=Course.objects.all()
       serializer=CourseSerializer(courses,many=True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CourseDetail(APIView):

        def get_object(self,id):
            try:
                return Course.objects.get(id=id)
            except:
                raise Http404
            
        def get(self,request,id):
            course=self.get_object(id)
            serializer=CourseSerializer(course)
            return Response(serializer.data)
        
        def put(self,request,id):
            course=self.get_object(id)
            serializer=CourseSerializer(course,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        def delete(self,request,id):
            course=self.get_object(id)
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
"""
            

    

