from django.urls import path
from App_auth.views import *
from.import views 
app_name = 'App_auth'

urlpatterns = [
    path('', home, name='home'),
    path('calander/', login_or_signup, name='login-or-signup'),
    path('logout/', logout_view, name='logout'),
    path('upload_file/', views.upload_file, name='upload-file'),
    path('function/',views.Function,name="function"),
    path('login-signup/',views.login_signup, name='login-signup'),
    path('prevsong/<int:song_id>/',views.prevsong,name ="prevsong"),
    path('nextsong/<int:song_id>',views.nextsong,name ="nextsong"),
    path('playsong/<int:song_id>',views.playsong,name ="playsong"),
    path('uber/',views.Uber,name="uber"),
    path('login/',views.Login,name='login'),
    path('register/',views.Register,name='register'),
    path('filter/',views.Template,name ='filter')
]

