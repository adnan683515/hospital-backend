
from rest_framework import serializers
from .models import Designation,Spealization,Doctor,AvailableTime,Review


class  DesignationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = "__all__"
        
class SpealizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Spealization
        fields = "__all__"
  
class AvailableTimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = "__all__"     
        
         
class DoctorSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    designation =  serializers.StringRelatedField(many=True)  # This is for reading
    spealization = serializers.StringRelatedField(many=True)  #
    available_time =  serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Doctor
        fields = "__all__"
     
        
class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        
