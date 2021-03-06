"""Postapp1 URL Configuration

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
    2. Add a URL to urlpatterns:  path('Post/', include('Post.urls'))
"""
from django.urls import include
from django.urls import path
from . import views


urlpatterns = [
    path('',views.PostList.as_view(),name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    #path('<slug:slug>/',views.PostDetail.as_view(),name='post_detail'),
]

# urlpatterns = [
#     path('',views.Posts),
# ]
