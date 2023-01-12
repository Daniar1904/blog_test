from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),  # accounts/register/
    path('', views.UserListView.as_view()),  # accounts/
    path('<int:pk>/', views.UserDetailView.as_view()),  # accounts/<id>/
]