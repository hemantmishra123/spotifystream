from django.urls import path
from App_auth.views import *
from.import views 

urlpatterns = [
    path('', home, name='home'),
    path('calander/', login_or_signup, name='login-or-signup'),
    path('login-signup', login_signup, name='login-signup'),
    path('logout/', logout_view, name='logout'),
    path('upload_file/', views.upload_file, name='upload-file'),
    path('function/',views.Function,name="function")
]

