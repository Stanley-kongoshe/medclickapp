from django.urls import path
from . import views

app_name = 'medclickapp'

urlpatterns = [
    path('', views.homepage, name='homepage'),

]
