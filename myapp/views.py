from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import employee
from . forms import employeeform

# Create your views here.
def home(request):
    d = {
        'title':'Home',
        'page':'Home Page',
        'data':'Hello Suresh, Good Afternoon',
        'page_color':'yellow',
        'content':'''Cyber security Fundamentals
Cybersecurity is the body of technologies, processes, and practices designed to protect networks, computers, programs and data from attack, damage or unauthorized access. The term cybersecurity refers to techniques and practices designed to protect digital data.
'''
    }
    response = render(request,'home.html',d)
    response.set_cookie('page', 'homepage')
    return response

def about(request):
    dt = {
        'title':'About',
        'page_color':'yellow',
        'page_data':'About Page'
    }
    response = render(request,'about.html',dt)
    response.set_cookie('page','about page')
    return response

def services(request):
    d = {
        'title':'Services',
        'tbldata':[['suresh','suresh@gmail.com'],
                   ['harish','harish@gmail.com'],
                   ['siva','siva@gmail.com'],
                   ['syed','syed@gmail.com']]
    }

    d = {
        'title':'Services',
        'tbldata':{'suresh':{'name':'suresh','email':'suresh@gmail.com'},
            'harish':{'name':'harish','email':'harish@gmail.com'},
            'siva':{'name':'siva','email':'siva@gmail.com'},
            'syed':{'name':'syed','email':'syed@gmail.com'}
        }
    }
    response = render(request,'services.html',d)
    response.set_cookie('page','services page')
    return response

def contact(request):
    dt = {
        'title':'Contact',
        'page_color':'yellow',
        'page_data':'Contact Page'
    }
    response = render(request,'contact.html',dt)
    response.set_cookie('page','contact page')
    return response

def save(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        address = request.POST['address']
        designation = request.POST['designation']
        #print(name,mobile,email,address,designation)
        e = employee()
        e.name = name
        e.mobile = mobile
        e.email = email
        e.address = address
        e.designation = designation
        e.save()
    return redirect(read)
    
@login_required(login_url='signin')
def read(request):
    records = employee.objects.all()
    dt={'records':records}
    return render(request,'read.html',dt)

def update(request):
    if request.method == 'GET':
        id = request.GET['id']
        name = request.GET['name']
        mobile = request.GET['mobile']
        email = request.GET['email']
        address = request.GET['address']
        designation = request.GET['designation']
    emp = employee.objects.get(id=id)
    emp.name = name
    emp.mobile = mobile
    emp.email = email
    emp.address = address
    emp.designation = designation
    emp.save()
    return HttpResponse('Record updated...')

def edit(request,id):
    emp = employee.objects.get(id=id)
    d = {'data':emp}

    return render(request,'edit.html',d)

def delete(request,id):
    emp = employee.objects.get(id=id)
    emp.delete()
    return redirect(read)

def insert(request):
    return render(request,'insert.html')

def signin(request):
    return render(request,'login.html')

def loggin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect(home)
    return HttpResponse('login failed')

def loggout(request):
    logout(request)
    return redirect(home)

def insertform(request):
    saved = False
    if request.method == 'POST':
        form = employeeform(request.POST)
        if form.is_valid():
            form.save()
            saved = True
            return HttpResponseRedirect('/form?saved=True')
    else:
        form = employeeform
        d = {'form':form}
        return render(request,'insertform.html',d)