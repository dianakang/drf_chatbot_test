from django.urls import path, include
from .views import helloAPI, randomChatbot

urlpatterns = [
    path('hello/', helloAPI),
    path('<int:id>/', randomChatbot),
]