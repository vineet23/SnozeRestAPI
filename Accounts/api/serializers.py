from rest_framework import serializers
from Accounts.models import Snoze_User
from django.contrib.auth.hashers import make_password
from Accounts.models import Snoze_User
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.validators import UniqueValidator

class User_Registration_API_Serializer(serializers.ModelSerializer):
    '''
        Serializer class that checks for the fields in the request
        and then creates the instance.
    '''
    # this checks whether the email is unique or no.
    email = serializers.EmailField(validators=[UniqueValidator(queryset=Snoze_User.objects.all(), message="The email is already registered.")])
    
    def create(self, validated_data):
        # this method has been overrided to change hash the password
        # manually, as the form would simply dump the normal string 
        # and would cause problems with the related user object
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])

        return super().create(validated_data)

    class Meta:
        # this class specifies the data about the outer class
        model = Snoze_User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'phone_number', 'profile_picture']