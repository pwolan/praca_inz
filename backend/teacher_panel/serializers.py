# from django.contrib.auth.models import User
from backbone.models import CustomUser as User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, serializers
from .models import Classroom, UserClassroom, Children




# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
        
#         # print(token)
#         # token['email'] = user.email 
#         # you can put any other fields you wish and within the user object
        
#         return token
#     def validate(self, attrs):
#         password = attrs.get("password")
#         email = attrs.get("email")
#         user = User.objects.get(email=email)
#         if user.check_password(password):
#             return {
#                 'token': jwt_encode_handler(payload),
#                 'user': user
#             }
#         else:
#             raise serializers.ValidationError("Wrong password")
    
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'
        
class UserClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClassroom
        fields = '__all__'

class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = '__all__'