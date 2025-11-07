from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from App1.models import Student
from App1.serializer import StudentSerializer

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
