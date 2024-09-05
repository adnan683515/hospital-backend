from django.shortcuts import render
from rest_framework import viewsets
from .serializers import appointmentSerializers
from .models import Appointment
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class appointmentViewSet(viewsets.ModelViewSet):

    
    queryset = Appointment.objects.all()
    serializer_class = appointmentSerializers
    
    
    #custom queryset korar jonno
    def get_queryset(self):
        queryset = super().get_queryset() #parent k inherit korlam(8 no line)
        # print(queryset)
        # print(self.request.query_params)
        
        patient_id = self.request.query_params.get('patient_id') 
        #patient_id hocce patient model ar akta primary key
        
        
        doctor_id = self.request.query_params.get('doctor_id')
        #doctor_id hocce doctor model ar akta primary key
        
        
        if doctor_id:
            #jdi doctor_id true hoi mane exits kore tah hole amder oi doctor ar apppointment gula show korbe
            queryset = queryset.filter(doctor_id=doctor_id)

        if patient_id : 
            # jdi patient_id true hoi mane exits kore tah hole amder oi patient ar apppointment gula show korbe
            queryset = queryset.filter(patient_id = patient_id)
            
        return queryset
    
    
    