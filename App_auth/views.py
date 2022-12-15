from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import json 
from .forms import UploadFileForm
from django.shortcuts import redirect
import pandas as pd 
import ast
from logging import *
from .models import Song,Image
from .serializers import *
Counter=0
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from App_auth.backends import UserBackend 
# Create your views here. 

def home(request):
    birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
    ariji_uri = 'https://open.spotify.com/artist/4IKVDbCSBTxBeAsMKjAuTs?si=R-mO_p7hTYWZ8TEQeG07Bg'
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id= '5e18ad9f4b704e67b5861ac09cc7d7d2',client_secret='f33a36a9221140a4bc1b3e8499af15d6'))
    songs=[]
    name="Armaan Malik"
    results = spotify.artist_top_tracks(ariji_uri)
    for track in results['tracks'][:10]:
        song=track['name']
        audio=track['preview_url']
        image = track['album']['images'][0]['url']
        
    for item in Song.objects.all():
        songs.append(item)

    queryset = Song.objects.all()
    serializer = SongSerializer(queryset,many=True)
    li= serializer.data 
    li=json.dumps(li)
    instance = Song.objects.get(id=9)
    context= {'songs':songs ,'data':instance,'music':li}
    return render(request,'App_auth/music.html',context)

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse("error")
        else:
            user = User(username = username,password = password)
            user.save()
            return redirect('/login/')
    return render(request,'App_auth/signup.html')


def Login(request):
    if request.method == 'POST':
        print("executed")
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        instance = UserBackend()
        print(instance.authenticate(request,username=username,password=password))
        user = User.objects.filter(username = username).first()
        if user:
            if password == user.password:
                return redirect('/home/')
            else:
                return HttpResponse('Wrong PASSWORD')
        else:
            return HttpResponse("notok")
        
    return render(request,'App_auth/register.html')

def prevsong(request,song_id):
    songs=[]
    for item in Song.objects.all():
            songs.append(item)

    if (song_id!=1):
        song_id-=1  
        instance = Song.objects.get(id=song_id)
        queryset = Song.objects.all()
        serializer = SongSerializer(queryset,many=True)
        li= serializer.data 
        li=json.dumps(li)
        context= {'songs':songs ,'data':instance,'music':li}
        return render(request,'App_auth/music.html',context)
    else:
        queryset= Song.objects.all()
        song_id = len(queryset)
        instance = Song.objects.get(id=song_id)
        serializer = SongSerializer(queryset,many=True)
        li= serializer.data 
        li=json.dumps(li)
        context= {'songs':songs ,'data':instance,'music':li}
        return render(request,'App_auth/music.html',context)

def Uber(request):
    return render(request,'App_auth/uber.html')



def nextsong(request,song_id):
    queryset = Song.objects.all()
    if (song_id<len(queryset)):
        song_id+=1
        songs=[]
        for item in Song.objects.all():
            songs.append(item)
            
        instance = Song.objects.get(id=song_id)
        context= {'songs':songs ,'data':instance}
        return render(request,'App_auth/music.html',context)

def playsong(request,song_id):
    songs=[]
    for item in Song.objects.all():
        songs.append(item)

    instance = Song.objects.get(id=song_id)
    queryset = Song.objects.all()
    serializer = SongSerializer(queryset,many=True)
    li= serializer.data 
    li=json.dumps(li)

    context= {'songs':songs ,'data':instance,'music':li}
    return render(request,'App_auth/music.html',context)


    

def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        handle_uploaded_file(myfile)
        df=FileRead(myfile)
        context={}
        mylist = zip(df['Key'], df['Value'])
        context= {'mylist':mylist}
        if(Counter==0):
            return render(request,'App_auth/music.html',context)
        
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
        return df

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
    return render(request,'App_auth/music.html')


def login_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            print("this is the Logined user hello i am here ")
            print(request.User)
            return render(request,'App_auth/music.html')
        else:
            print("this method is wo")
            createUser = User(username=email)
            createUser.set_password(password)
            createUser.save()
            user = authenticate(username=email, password=password)
            login(request, user)
            return render(request,'App_auth/music.html')

    return render(request,'App_auth/login_or_signup.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_auth:login-or-signup'))

