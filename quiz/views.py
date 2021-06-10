from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response('hello world')

@api_view(['GET'])
def randomQuiz(request, id):# 필요한 무작위 퀴즈의 수를 입력하면 퀴즈들을 출력해줌
    totalQuizs = Quiz.objects.all()#전체 퀴즈를 저장하는 변수
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many=True)
    return Response(serializer.data)