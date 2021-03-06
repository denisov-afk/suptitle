"""zubtitle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from website import views


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.WebsiteLoginView.as_view(), name='login'),
    path('accounts/logout/', views.WebsiteLogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
    path('addvideo/', views.add_video, name='add_video'),
    path('delvideo/<int:id>/', views.del_video, name='del_video'),
    path('editvideo/<int:pk>/', views.VideoUpdateView.as_view(), name='edit_video'),

    path('<str:pagename>/', views.page, name='page'),

    path('api/video/<int:pk>/', views.api_get_video, name='api_get_video'),
    path('api/video-captions/<int:pk>/', views.api_video_captions_path, name='api_video_captions_path'),
    path('send-video-for-processing/<int:pk>/', views.send_video_on_processing, name='send_video_on_processing'),

]
