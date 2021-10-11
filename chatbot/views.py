from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Chatbot
from .serializers import ChatbotSerializer
import random

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response('hello world!')

@api_view(['GET'])
def randomChatbot(request, id):
    totalChats = Chatbot.objects.all()
    randomChats = random.sample(list(totalChats), id)
    serializer = ChatbotSerializer(randomChats, many=True)
    return Response(serializer.data)