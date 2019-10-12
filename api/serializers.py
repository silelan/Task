from rest_framework import serializers
from accounts.models import Profile

from rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    name = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(required=True)
    
    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
                'password1': self.validated_data.get('password1', ''),
                'email': self.validated_data.get('email', ''),
                'name': self.validated_data.get('name', ''),
                'date_of_birth': self.validated_data.get('date_of_birth', ''),
            }

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('email','name','date_of_birth')
        read_only_fields = ('email',)

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        data = Profile.objects.all()
        fields = ['id','user','gender','profile_picture','permanent_address','friends']

