from django.urls import path
from . import views


#URLconfig
urlpatterns=[
    path('',views.say_hello)
]