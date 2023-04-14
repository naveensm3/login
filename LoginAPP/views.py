from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render

from LoginAPP.models import City, Course, Student

# Create your views here.
def home(request):
    return render(request,'login.html')

def login_fun(request):
    return render(request,'register.html')

def register_fun(request):
    return render(request,'register.html')


def read_register(request):
    uname=request.POST['tbname']
    email=request.POST['tbemail']
    password=request.POST['tbpass']
    user=User.objects.create_superuser(username=uname,email=email,password=password)
    user.save()
    return render(request,'login.html',{'msg':f'user created successfully username is {uname}'})


def read_login(request):
    uname=request.POST['tbname']
    password=request.POST['tbpass']
    user=authenticate(username=uname,password=password)
    if user is not None:
        login(request,user)
        b1 = Student.objects.all()
        return render(request,'index.html',{'data':b1})
    else:
        return render(request,'login.html')

def logout_fun(request):
    logout(request)
    return redirect('login')

def addstudent(request):
    cities = City.objects.all()
    course = Course.objects.all()
    return render(request,'addstudent.html',{'cities':cities,'course':course})


def readstudentdata(request):
    s = Student()
    s.fname = request.POST['tbfname']
    s.lname = request.POST['tblname']
    s.mobile = request.POST['tbmobile']
    s.email = request.POST['tbemail']
    s.city_name =City.objects.get(city_name= request.POST['ddlcity'])
    s.course_name = Course.objects.get(course_name=request.POST['ddlcourse'])
    s.save()
    s = Student.objects.all()
    return render(request,'displaystudents.html',{'data':s})

def display_fun(request):
    b1=Student.objects.all()
    return render(request,'displaystudents.html',{'data':b1})

def updatedata_fun(request,id):
    b1=Student.objects.get(id=id)
    if request.method == 'POST':
        b1.fname =request.POST['tbfname']
        b1.lname = request.POST['tblname']
        b1.mobile = request.POST['tbmobile']
        b1.email = request.POST['tbemail']
        b1.city_name = City.objects.get(city_name=request.POST['ddlcity'])
        b1.course_name = Course.objects.get(course_name=request.POST['ddlcourse'])
        b1.save()
        return redirect('display')
    return render(request,'studentdata.html',{'data':b1})

def deletedata_fun(request,id):
    b1=Student.objects.get(id=id)
    b1.delete()
    return redirect('display')


