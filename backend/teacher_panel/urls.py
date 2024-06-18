from django.urls import path
from . import views
from rest_framework_simplejwt.views import  TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path("", views.teacher_data),
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("class/<int:id>", views.class_data),
    path('class/create', views.create_classroom, name='create_classroom'),
    path('class/<int:id>/create', views.create_child, name='create_child')
]