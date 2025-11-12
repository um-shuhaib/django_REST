from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from App1.models import Student
from App1.serializer import StudentSerializer,StudentModelSerializer
from rest_framework import status

# Create your views here.
class Home(APIView):
    def get(self,request):
        return Response({"msg":"hallooo"})
    
    def post(self,request):
        return Response({"msg":"guyzz"})
    

class StudentView(APIView):
    def get(self,request):
        student=Student.objects.all()
        res=StudentSerializer(student,many=True)
        return Response(data=res.data)
    def post(self,request):
        name=request.data.get("name")
        place=request.data.get("place")
        age=request.data.get("age")
        Student.objects.create(name=name,place=place,age=age)
        return Response({"msg":"student added"})
    
class SudentDetailView(APIView):
    def get(self,request,**kwargs):
        try:
            stud=Student.objects.get(id=kwargs.get("id"))
            serialize=StudentSerializer(stud)
            return Response(data=serialize.data)
        except:
            return Response({"msg":"DOUS NOT EXIST"},status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,**kwargs):
        stud=Student.objects.get(id=kwargs.get("id"))
        stud.delete()
        return Response({"msg":"data deleted"})
    
    def put(self,request,**kwargs):                          #update
        stud=Student.objects.get(id=kwargs.get("id"))
        stud.name = request.data.get("name")
        stud.place = request.data.get("place")
        stud.age = request.data.get("age")
        stud.save()
        return Response({"msg":"data updated"})

class StudentModelView(APIView):
    def get(self,request):
        student=Student.objects.all()
        serialiser=StudentModelSerializer(student,many=True)
        return Response(data=serialiser.data)
    def post(self,request):
        serialiser=StudentModelSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(data=serialiser.data)
        else:
            return Response(data=serialiser.errors)

class StudentModelDetailView(APIView):
    def get(self,request,**kwargs):
        stud=Student.objects.get(id=kwargs.get("id"))
        serializer=StudentModelSerializer(stud)
        return Response(data=serializer.data)
    def delete(self,request,**kwargs):
        Student.objects.get(id=kwargs.get("id")).delete()
        return Response({"msg":"data deleted"})
    def put(self,request,**kwargs):
        stud=Student.objects.get(id=kwargs.get("id"))
        serializer=StudentModelSerializer(stud,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"data updated"})

