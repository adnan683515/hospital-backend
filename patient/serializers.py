from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User



class patientSerializers(serializers.ModelSerializer):
    # user= serializers.StringRelatedField(many=False)
    class Meta:
        model = Patient
        fields = "__all__"
        
        
class RegistrationSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password']
    
    
    def save(self):
        username= self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password1 = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        
        if password1 != password2:
            raise serializers.ValidationError({'error':"Password doesn't match"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':"This email already exit"})
        
        account = User(username=username,first_name=first_name,last_name=last_name,email=email)
        
        account.set_password(password1)
        account.is_active= False
        account.save()
        
        return account
    
    




class loginSerializers(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
    
    
    