from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,UpdateAPIView,DestroyAPIView

from drf_yasg.utils import swagger_auto_schema
from .serializer import RegisterSerializer

User = get_user_model()

#создаем класс, для регистрации и добавляем декакаратор для swagger для фронтендщиков
class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer())
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

#класс предстовления дял того что бд найти пользавателя и актировать его
class ActivationView(APIView):
    #переопределяем метод get для того чтобы найти пользавателя по имейлу и акт-коду ведь они уникальны
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response('пользаватель не найден', 404)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Вы успешно активировали аккаунт', 200)
    

class GetUserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

#В классе DeleteUpdate наследуемся от двух классов для обновление и удалени ведь и том и другом надо найти запись по ID
class DeleteUpdateUser(DestroyAPIView, UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    lookup_field = 'id'





