"""OAuth_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from App_auth import views
from rest_framework.routers import DefaultRouter 
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('App_auth.urls')),
    path('betterui/',views.BetterUi,name='betterui'),
    path('',views.home,name='home'),
    path('login-signup/', views.login_signup, name='login-signup'),

    path('oauth/', include('social_django.urls', namespace='social')),
    path('uber/',views.Uber,name="uber"),
    path('gettoken/',TokenObtainPairView.as_view(),name= 'Token_refresh'),
    path('refreshtoken/',TokenRefreshView.as_view(),name= 'Token_refresh'),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
