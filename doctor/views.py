from django.shortcuts import render
from rest_framework import viewsets,pagination,filters
from .models import Designation,Spealization,Doctor,AvailableTime,Review
from .serializers import DesignationSerializers,SpealizationSerializers,DoctorSerializers,ReviewSerializers,AvailableTimeSerializers
# Create your views here.
from rest_framework.permissions import IsAuthenticatedOrReadOnly




#ai model view set diya amra api  ta (post,put,delete,get) sob e korte parbo

class DesignationviewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializers
    

class SpeacializationtionviewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
    queryset = Spealization.objects.all()
    serializer_class = SpealizationSerializers
    
class DoctorPagination(pagination.PageNumberPagination):
    page_size =1
    page_query_param = 'page_size'
    max_page_size = 100
    
class DoctorviewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset= Doctor.objects.all()
    serializer_class = DoctorSerializers
    
    pagination_class = DoctorPagination
    

class AvailableTime_SpecepicDoctor(filters.BaseFilterBackend):
    
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return queryset.filter(doctor = doctor_id)
        return queryset
    
    
    
    
class AvailableTimeviewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset= AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializers
    filter_backends = [AvailableTime_SpecepicDoctor]
    
    
