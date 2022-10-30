from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import json 
from .forms import UploadFileForm
import pandas as pd 
import ast
from logging import *
Counter=0
# Create your views here.
def home(request):
    return render(request, 'App_auth/home.html')


def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        handle_uploaded_file(myfile)
        FileRead(myfile)
        if(Counter==0):
            return HttpResponse("File is uploaded succesfully")
        
        else:
            return HttpResponse("Please Upload a Valid Json File.")
   
    else:
        return render(request, 'App_auth/upload.html')

def handle_uploaded_file(f):
    with open('App_auth/FileFolder/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
             destination.write(chunk)

#Read File and seprate it into the Chunks and save it into the Directory.
def FileRead(f):
    print(f.name)
    global Counter
    Counter=0
    f = open('App_auth/FileFolder/'+f.name)
    try:
        arr = json.load(f)
        Key=[]
        Value=[]
        print(type(arr))
        for key in arr.keys():
            Key.append(key)
        for value in arr.values():
            Value.append(value) 
        stack=[]
        count=0
        for j in Value:
            if type(j) is dict:
                stack.append(count)
            count+=1
    #First Level of the Json Data printing.
        data_tuples = list(zip(Key,Value))
        basicConfig(filename='logfile.log',level=DEBUG,filemode='w') 
        debug("File is uploaded succesfully.")
        df = pd.DataFrame(data_tuples, columns=['Key','Value'])
        print(df)
        print(stack,"showing all Locations of dict Data ")
        for i in stack:
            print(i)

    except ValueError as err:
        basicConfig(filename='logfile.log',level=DEBUG,filemode='w') 
        error("This is Not a Valid Json Files Please Upload a valid json Files")
        Counter=1

def Function():
    import sys
    f = open(sys.argv[1],'r')
    arr=json.load(f)
    print(arr)

def login_or_signup(request):
    return render(request, 'App_auth/login_or_signup.html')


def login_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            print("this is the Logined user hello i am here ")
            print(request.User)
            return HttpResponseRedirect(reverse('App_main:home'))
        else:
            print("this method is wo")
            createUser = User(username=email)
            createUser.set_password(password)
            createUser.save()
            user = authenticate(username=email, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('App_main:home'))

    return HttpResponseRedirect(reverse('App_auth:login-signup'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_auth:login-or-signup'))

