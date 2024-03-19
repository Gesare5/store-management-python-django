from django.urls import path
from .views import GenericUserAPIView, UserAPIView, CustomRegisterView

urlpatterns = [
    path("", UserAPIView.as_view()),
    path("<int:id>/", GenericUserAPIView.as_view()),
    path("register/", CustomRegisterView.as_view()),
]
