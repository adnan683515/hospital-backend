from django.contrib import admin
from appointment.models import Appointment

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient','doctor','time','symptom','appointment_type','appointment_status','cencel']
    
    def p_first_name(self,obj):
        return obj.patient.user.first_name
    
    
    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appointment_status == 'Running' and obj.appointment_type=='online':
            mail_sub = 'Your online Appointment accepted Please below the link'
            email_body = render_to_string('appointment.html',{'user':obj.patient.user,'doctor':obj.doctor})
            email = EmailMultiAlternatives(mail_sub,'',to=[obj.patient.user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            
            
admin.site.register(Appointment,AppointmentAdmin)