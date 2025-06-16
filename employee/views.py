from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee,Student
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser


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
    


