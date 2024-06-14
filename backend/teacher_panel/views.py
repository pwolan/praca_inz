from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *

@api_view(['GET'])
def send_some_data(request):
    classes = dict()
    # TODO jak ktoś zrobi logowanie to należy podmienić kod
    # user_classes = UserClassrooms.objects.filter(user_id=request.user.id)
    user_classes = UserClassrooms.objects.filter(user_id=1)
    for class_obj in user_classes:
         classes[class_obj.classroom_id] = Classroom.objects.get(id=class_obj.classroom_id).name
    return Response({
        "data": "Hello from techer api",
        "classes": classes
    })

@api_view(['GET'])
def class_data(request, id):
    # obj = Children(1, 'jan', 'augustyn', 1)
    # obj.save()
    # obj = Children(2, 'jakub', 'bizan', 1)
    # obj.save()
    # obj = Children(3, 'jan', 'bizan', 2)
    # obj.save()
    # obj = Children(4, 'paweł', 'wolanin', 2)
    # obj.save()
    # obj = Children(5, 'ja', 'kroczek', 1)
    # obj.save()
    children = dict()
    objects = Children.objects.filter(classroom_id=id)
    for obj in objects:
        children[obj.id] = {'name': obj.name, 'surname': obj.surname}
    return Response({
        "id": id,
        "children": children
    })

class HomeView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {
            'message': 'Welcome to the JWT Authentication page using React Js and Django!'
        }
        return Response(content)
    

class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
          
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response(status=status.HTTP_400_BAD_REQUEST)