from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee,Student
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser

from rest_framework.authtoken.models import Token
from .serializers import EmployeeSerializer, StudentSerializer
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin

from rest_framework.generics import GenericAPIView

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

 


def add_emp(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():          
            form.save()
            return redirect(request,'show.html')
        else:
            form=EmployeeForm()
            context={"form":form}
            return render(request,"edit.html",context) 
        
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  

def edit(request,id):
    e=Employee.objects.get(id=id)
    return render(request,"edit.html",{"Employee":e})

def update(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    context={"employee":employee}
    return redirect(request,"edit.html",context)
    
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")


def dashboard(request):  
    employee = Employee.objects.all() 
    return render(request,"dashboard.html") 

def count_visit(request):
    visit=request.session.get("visit",0)+1
    request.session['visit']=visit
    return HttpResponse(f"Visit count:{visit}")     

def student_info(request, id):
    try:
        student = Student.objects.get(id=id)
        return render(request, 'student.html', {'student': student})
    except Student.DoesNotExist:
        return HttpResponseNotFound("Student not found.")

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})



class LCStudentList(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes = [IsAdminUser]

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)



class RUDStudentRetrive(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)    
    



class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    


# employee/views.py

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class LoginView(APIView):
    """
    Accepts username and password, returns auth token if valid.
    """

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Username and password are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {"error": "Invalid username or password."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "username": user.username,
            "email": user.email
        }, status=status.HTTP_200_OK)
