from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask')  
]

# 12700.8000/todo/addTask/