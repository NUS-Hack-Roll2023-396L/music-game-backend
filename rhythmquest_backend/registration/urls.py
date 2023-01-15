from django.urls import path
from registration import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('create_user/', views.UserCreate.as_view()),
]
