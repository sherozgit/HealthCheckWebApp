from django.urls import path
from . import views 

urlpatterns = [
    path('', views.departmentleader, name='departmentleader'),

]