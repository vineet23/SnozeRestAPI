from rest_framework import generics
from .import serializers
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser
from Accounts.models import Snoze_User
from rest_framework import status as code
from Accounts.api.serializers import User_Registration_API_Serializer

class User_Registration_API_View(generics.CreateAPIView):
    '''
        A class that creates the a Snoze_user instance and stores it to the database
    '''
    serializer_class = serializers.User_Registration_API_Serializer
    # this class specifies that this view is only accessible by staff users
    permission_classes = (IsAdminUser, )

class User_Deactivate_API_View(APIView):
    permission_classes = (IsAdminUser, )

    def post(self, request, format=None):
        data = {
                'deactivate failed' :'Account deactivation failed',
            }
        # the token variable will be passed as a post Parameter
        if 'token' in request.POST:
            token = request.POST['token']
            try:
                # check if the token exists 
                user = Token.objects.get(key=token).user
            except ObjectDoesNotExist:
                # if does not exist return 400 error
                return Response(data=data, status=400)
            
            user.is_active = False
            user.save()
            data = {
                'deactivation success' :'Account deactivated successfully',
            }
            # if the user is deactivated successfully return success 200
            return Response(data=data, status=200)
            
class UserExistsAPIView(APIView):
    permission_classes = (IsAdminUser, )

    def post(self, request, format=None):
        if 'username' in request.POST:
            username = request.POST['username']
            try:
                # Check if username is taken in the snoze_user 
                Snoze_User.objects.get(username=username)
                data = {
                    "failed": "username taken",
                }
                return Response(data=data, status=code.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                # username does not exist, can take this username
                data = {
                    "success": "Username available.",
                }
                return Response(data=data, status=code.HTTP_200_OK)




class All_User_API_View(APIView):

    def get(self, request):
        all_user = Snoze_User.objects.all()
        serializer = User_Registration_API_Serializer(all_user, many=True)
        return Response(serializer.data)

    def post(self):
        pass