from django.urls import path, include
from .views import helloAPI, randomQuiz

urlpatterns = [
    path("hello/", helloAPI),# 해당 url이 넘어왔을 때 뒤쪽의 view를 보내줌
    path("<int:id>/", randomQuiz),# 새 모델을 사용하려면 migration을 해줘야함
]