from django.urls import path
from accounts import views

urlpatterns = [
    path('user/create/', views.CreateUserView.as_view()),
]
