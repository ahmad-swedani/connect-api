from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        

        token = super().get_token(user)
        token["email"] = user.email
        token["password"] = user.password
        return token

class MyTokenObtainPairCustomView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer