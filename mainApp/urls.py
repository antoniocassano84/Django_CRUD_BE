from django.urls import path
from mainApp.views import *

urlpatterns = [
    path('<int:pk>', DetailToDo.as_view()),
    path('', ListToDo.as_view()),
    path('create', CreateToDo.as_view()),
    path('delete/<int:pk>', DeleteToDo.as_view())
]