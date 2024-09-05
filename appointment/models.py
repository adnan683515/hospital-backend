from django.db import models
from patient.models import Patient
from doctor.models import Doctor,AvailableTime
# Create your models here.
APPOINTMENT_Type = [
    ('online','online'),
    ('offline','offline')
]

APPOINTMENT_STATUS = [
    
    ('pending','pending'),
    ('Running','Running'),
    ('Compleated','Compleated')
]

class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor  = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    time = models.ForeignKey(AvailableTime,on_delete=models.CASCADE)
    appointment_type = models.CharField(choices=APPOINTMENT_Type,max_length=100)
    appointment_status = models.CharField(choices=APPOINTMENT_STATUS,max_length=100)
    symptom =models.TextField()
    cencel =models.BooleanField(default=False)  
    
    def __str__(self):
        return f"Patien:{self.patient.user.first_name} Doctor:{self.doctor.user.first_name},Time:{self.time},Symptom:{self.symptom} ,Appointment Type:{self.appointment_type},Appointment Status : {self.appointment_status}"
    