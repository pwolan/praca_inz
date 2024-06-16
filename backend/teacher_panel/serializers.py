# from django.contrib.auth.models import User
from backbone.models import CustomUser as User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, serializers
from .models import Classroom, UserClassroom

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        print(token)
        token['email'] = user.email #TODO change to email
        # you can put any other fields you wish and within the user object
        return token
    
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'
        
class UserClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClassroom
        fields = '__all__'