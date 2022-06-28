from django.urls import path
from .views import RegisterView,RegisterReturn
#  LogoutAPIView, LoginAPIView
from .views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('register/<int:pk>/', RegisterReturn.as_view(), name="register_detail"),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
