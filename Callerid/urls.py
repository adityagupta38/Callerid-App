"""Callerid URL Configuration

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
from callinfo import views
from rest_framework import routers
from callinfo import apiviews


router = routers.DefaultRouter()
router.register('gusersapi', apiviews.GlobalUsersApi, basename='gusersapi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name='user_login'),
    path('', include(router.urls)),
    path('rest_api', include('rest_framework.urls')),
    path('userregisteration', views.user_registeration, name='user_registeration'),
    path('userhome', views.user_home, name='user_home'),
    path('globalusers', views.global_user, name='global_users'),
    path('searchbyname', views.search_by_name, name='search_by_name'),
    path('searchbynumber', views.search_by_number, name='search_by_number'),
    path('addspam', views.add_update_spam, name='add_update_spam'),
    path('userlogout', views.user_logout, name='user_logout'),
]
