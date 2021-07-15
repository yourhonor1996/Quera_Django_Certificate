from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
import rest_framework.status as status
from .serializers import UserSerializer
login = obtain_auth_token


class Logout(APIView):
    """
    Delete user's authtoken
    """
    permission_classes = (IsAuthenticated, )
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response(data= {'message': f'Bye {request.user.username}!'}, status= status.HTTP_204_NO_CONTENT)


class Register(CreateAPIView):
    """
    Create a new user
    """
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
        data = serializer.data
        return Response({'id': data['id'], 'username': data['username']}, status=status.HTTP_201_CREATED)


    
    
        
