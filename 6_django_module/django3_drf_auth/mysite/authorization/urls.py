from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authorization import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),

    path('register/', views.RegistrationView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

