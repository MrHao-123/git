from django.urls import path
from . import views

urlpatterns = [
    path('',views.aa,name='aa'),
    path('login/',views.login ,name='login')
]