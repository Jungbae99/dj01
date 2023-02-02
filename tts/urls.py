from django.urls import path
from . import views

app_name="tts"
urlpatterns = [
      path('index/', views.index, name='index'),
] 
