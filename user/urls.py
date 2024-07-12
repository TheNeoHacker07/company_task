from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ActivationView, GetUserList, DeleteUpdateUser

urlpatterns=[
    path('registers/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    # url для активации юзера после регистрации
    path('active/<str:email>/<str:activation_code>/', ActivationView.as_view()),
    
    # url для удаления,обновление и получения списка пользавателей
    path('user_list/', GetUserList.as_view()),
    path('user_delete/<int:id>/', DeleteUpdateUser.as_view()),
    path('user_update/<int:id>/', DeleteUpdateUser.as_view())

]