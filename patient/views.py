from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import Patient
from .serializers import patientSerializers,RegistrationSerializers,loginSerializers
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator 
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from rest_framework.authtoken.models import Token
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class petaintViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    
    queryset = Patient.objects.all()
    serializer_class = patientSerializers
    
    
class RegisterViewSet(APIView):
    serializer_class = RegistrationSerializers
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            #token banalam
            token = default_token_generator.make_token(user)
            print("TOken",token)
            #akta user ar jonno uid banalam
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("UID",uid)
            
            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"
            
            print(confirm_link)
            
            email_subject = "Email varification"
            email_body = render_to_string('confirm_email.html',{'confirm_link':confirm_link})
            email = EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            
            return Response("Check your mail!")
        
        return Response(serializer.errors)
    
    
def activate(request,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        print("Uid",uid)
        user = User._default_manager.get(pk=uid)
        print("USEr",user)
        
    except(User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect('login')
    else:
        return redirect('register')
        
        
    
    
class LoginViews(APIView):
    
    def post(self,request):
        serializer = loginSerializers(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username,password=password)
            if user:
                token,_ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request,user)
                return Response({'token':token.key,'user_id':user.pk})
            else:
                return Response('User Does not Exits')
        else:
            return Response(serializer.errors)
        
        
class logoutView(APIView):
    
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')