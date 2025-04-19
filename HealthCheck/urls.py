"""
URL configuration for HealthCheck project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.shortcuts import redirect 

def redirect_to_leader(request):
    return redirect('/departmentleader/')


urlpatterns = [
    path('', redirect_to_leader, name='redirect_to_leader'),
    path('admin/', admin.site.urls),
    path('departmentleader/', include('teams.urls')),
     # Voting functionality
    path('vote/', include('vote.urls')),
    # # User registration, login, profile, etc.
    # path('users/', include('users.urls')),
    
    
]
